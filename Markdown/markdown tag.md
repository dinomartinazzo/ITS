# Headings

# Heading level 1
## Heading level 2
### Heading level 3
#### Heading level 4
##### Heading level 5
###### Heading level 6

## Colors

Some Markdown text with <span style="color:blue">some *blue* text</span>.  
<span style="color:blue">some *This is Blue italic.* text</span>  
<span style="color:red">some **This is Red Bold.** text</span>  

<style>
	r { color: Red }
	o { color: Orange }
	g { color: Green }
</style>

#### TODOs:

- <r>TODO:</r> Important thing to do
- <o>TODO:</o> Less important thing to do
- <g>DONE:</g> Breath deeply and improve karma

## Paragraphs  
To create paragraphs, use a blank line to separate one or more lines of text.  
Don't put tabs or spaces in front of your paragraphs.

Keep lines left-aligned like this.

## Horizontal Rules

To create a horizontal rule, use three or more asterisks (***),    
dashes (---), or underscores (___) on a line by themselves.  

***  

## Line Breaks

To create a line break or new line end a line with two or more spaces,  
and then type return.  

Ho messo **due spazi a fine riga precedente**.

## Emphasis

I just love **bold text**.  
Love**is**bold    
Italicized text is the *cat's meow*.  
***Bold and Italic***
This text is ***really important***.  
This is really***very***important text.  

## Blockquotes

To create a blockquote, add a > in front of a paragraph.
> Dorothy followed her through many of the beautiful rooms in her castle.  

> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

> Dorothy followed her through many of the beautiful rooms in her castle.
>
>> The Witch bade her clean the pots and kettles  
and sweep the floor and keep the fire fed with wood.

  
> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>  *Everything* is going according to **plan**.

## Ordered Lists

1. First item
2. Second item
3. Third item
4. Fourth item    
 
```
```
1. First item
2. Second item
3. Third item
    1. Indented item
    2. Indented item
4. Fourth item   
``` 
```
1. First item
2. Second item
3. Third item
    - Indented item
    - Indented item
4. Fourth item

## Unordered Lists

- First item
- Second item
- Third item
- Fourth item 
    - Indented item
    - Indented item
- Fourth item 

Starting Unordered List Items With Numbers
- 1968\. A great year!
- I think 1969 was second best. 

## Adding Elements in Lists

To add another element in a list while preserving the continuity of the list,  
**indent the element four spaces or one tab**,   
as shown in the following examples.

* This is the first list item.
* Here's the second list item.

    > A blockquote would look great below the second list item.
	
* And here's the third list item.

## Task Lists

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media


## Code Blocks

Code blocks are normally indented four spaces or one tab.   
When they’re in a list, indent them eight spaces or two tabs.

1. Open the file.
2. Find the following code block on line 21:

        <html>
          <head>
            <title>Test</title>
          </head>

3. Update the title to match the name of your website.


## Images

1. Open the file containing the Linux mascot.
2. Marvel at its beauty.

    ![Tux, the Linux mascot](./tux.png)

3. Close the file.

The rendered output looks like this:

    Open the file containing the Linux mascot.

    Marvel at its beauty.

    Tux, the Linux mascot
    Close the file.

## Linking Images

[![An old rock in the desert](./tux.png "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)

## Code

At the command prompt, type `nano`.  
``Use `code` in your Markdown file.``  

To create code blocks, indent every line of the block by at least four spaces or one tab.

    <html>
      <head>
      </head>
    </html>

## Highlight
I need to highlight these ==very important words==.

## Subscript
To create a subscript, use one tilde symbol (~) before and after the characters.

H~2~O

## Superscript
 To create a superscript, use one caret symbol (^) before and after the characters.
 
X^2^

## Syntax Highlighting

```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

# Ruby Example

```ruby
x = 5 + 6
puts "Hello World! #{x}"
```

# C Example

```c
int main() {
  int y = SOME_MACRO_REFERENCE;
  int x = 5 + 6;
  cout << "Hello World! " << x << std::endl();
}
```

# C++ Example

```cpp
int main() {
  int y = SOME_MACRO_REFERENCE;
  int x = 5 + 6;
  cout << "Hello World! " << x << std::endl();
}
```
# C# Example

```c#
int main() {
  int y = SOME_MACRO_REFERENCE;
  int x = 5 + 6;
  cout << "Hello World! " << x << std::endl();
}
```

 
## Links

My favorite search engine is [Duck Duck Go](https://duckduckgo.com).  
My favorite search engine is [Duck Duck Go](https://duckduckgo.com "The best search engine for privacy").

## URLs and Email Addresses

To quickly turn a URL or email address into a link, enclose it in angle brackets.

<https://www.markdownguide.org>  
<fake@example.com>

I love supporting the **[EFF](https://eff.org)**.  
This is the *[Markdown Guide](https://www.markdownguide.org)*.  
See the section on [`code`](#code).

## Tables

| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |
| a   | b        | c      |
| d   | e        | f      |
| a   | b        | c      |
| d   | e        | f      |
| a   | b        | c      |
| d   | e        | f      |



## Heading IDs

### My Great Heading {#custom-id}

[Heading IDs](#heading-ids)

## Emoji  
https://gist.github.com/rxaviers/7360908


## Footnotes

Here's a simple footnote,[^1] and here's a longer one.[^bignote]

[^1]: This is the first footnote.

[^bignote]: Here's one with multiple paragraphs and code.

    Indent paragraphs to include them in the footnote.

    `{ my code }`

    Add as many paragraphs as you like.
	



