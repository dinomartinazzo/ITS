#!/usr/bin/env python3
"""Controlla i file correnti e ricrea gli ZIP; non rigenera schema, PCB o Gerber."""
from pathlib import Path
import json
import os
import sys
import tempfile
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'verifiche'))
from verifica_pcb import report


def package(target, files):
    fd, tmp = tempfile.mkstemp(prefix=target.stem+'-', suffix='.zip', dir=target.parent)
    os.close(fd)
    try:
        with ZipFile(tmp, 'w', ZIP_DEFLATED) as z:
            for path, name in files:
                z.write(path, name)
        with ZipFile(tmp) as z:
            assert z.testzip() is None
            for path, name in files:
                assert z.read(name) == path.read_bytes()
        os.replace(tmp, target)
    finally:
        if os.path.exists(tmp): os.unlink(tmp)


def main():
    result = report()  # Ogni errore ferma il processo prima di toccare gli ZIP.
    name = 'simulatore_ponte_348_p3'
    native = ROOT/'pcb'/name
    easy = ROOT/'pcb/easyeda'
    package(easy/'easyeda_solo_pcb_kicad51.zip', [(easy/(name+'.kicad_pcb'),name+'.kicad_pcb')])
    package(easy/'easyeda_progetto_kicad51.zip',
            [(easy/(name+ext),name+ext) for ext in ('.sch','-cache.lib','.kicad_pcb','.pro')])
    paths = [native/(name+ext) for ext in ('.kicad_pro','.kicad_sch','.kicad_pcb')]
    paths += [native/'fp-lib-table'] + sorted((native/'Simulatore.pretty').glob('*.kicad_mod'))
    package(easy/'easyeda_progetto_kicad7_non_dichiarato.zip',
            [(p,str(p.relative_to(native))) for p in paths])
    # Il job Gerber non è richiesto dai due importatori; includere tutti i livelli e i fori.
    gerbers = [(p,p.name) for p in sorted((native/'gerber').iterdir()) if p.suffix != '.gbrjob']
    for target in (easy/'easyeda_gerber.zip', ROOT/'pcb/jlcpcb'/f'{name}_gerber_JLCPCB.zip'):
        package(target,gerbers)
    (ROOT/'verifiche/pcb.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print('5 ZIP aggiornati e verificati; 32 pin e valori coerenti. Importazione EasyEDA non provata.')


if __name__ == '__main__':
    main()
