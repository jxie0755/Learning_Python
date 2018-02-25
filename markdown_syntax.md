Copied From [Markdown Syntax.md](https://github.com/fletcher/MultiMarkdown/blob/master/Documentation/Markdown%20Syntax.md)

## Phrase Emphasis ##

	*italic*   **bold**
	_italic_   __bold__


## Links ##

Inline:

	An [example](http://url.com/ "Title")

Reference-style labels (titles are optional):

	An [example][id]. Then, anywhere
	else in the doc, define the link:

	  [id]: http://example.com/  "Title"


## Images ##

Inline (titles are optional):

	![alt text](/path/img.jpg "Title")

Reference-style:

	![alt text][id]

	[id]: /url/to/img.jpg "Title"


## Headers ##

Setext-style:

	Header 1
	========

	Header 2
	--------

atx-style (closing #'s are optional):

	# Header 1 #

	## Header 2 ##

	###### Header 6


## Lists ##

Ordered, without paragraphs:

	1.  Foo
	2.  Bar

Unordered, with paragraphs:

	*   A list item.

		With multiple paragraphs.

	*   Bar

You can nest them:

	*   Abacus
		* answer
	*   Bubbles
		1.  bunk
		2.  bupkis
			* BELITTLER
		3. burper
	*   Cunning


## Blockquotes ##

	> Email-style angle brackets
	> are used for blockquotes.

	> > And, they can be nested.

	> #### Headers in blockquotes
	>
	> * You can quote a list.
	> * Etc.


## Code Spans ##

	`<code>` spans are delimited
	by backticks.

	You can include literal backticks
	like `` `this` ``.


## Preformatted Code Blocks ##

Indent every line of a code block by at least 4 spaces or 1 tab.

	This is a normal paragraph.

	    This is a preformatted
	    code block.


## Horizontal Rules ##

Three or more dashes or asterisks:

	---

	* * *

	- - - -


## Manual Line Breaks ##

End a line with two or more spaces:

	Roses are red,
	Violets are blue.


标题：
# h1级标题 #
## h2级标题 ##
### h3级标题 ###
#### h4级标题 ####
##### h5级标题 ####
###### h6级标题 ######

分割线：三个以上的短线 即可作出分割线

----

超链接：[连接名称](网址 , 标题)
[我是链接名](http://www.izhangbo.cn, "我是标题")
[<i class="icon-refresh"></i> 点我刷新](/sonfilename/)

另一种超链接写法：[链接名][链接代号]
[here][3]
然后在别的地方定义 3 这个详细链接信息，
[3]: http://www.izhangbo.cn "聚牛团队"

直接展示链接的写法：<http://www.izhangbo.cn>

键盘键
<kbd>Ctrl+[</kbd> and <kbd>Ctrl+]</kbd>

code格式：反引号
Use the `printf()` function.

``There is a literal backtick (`) here.针对在代码区段内插入反引号的情况``

强调：
*斜体强调*
**粗体强调**

图片
![Alt text](http://www.izhangbo.cn/wp-content/themes/minty/img/logo.png "Optional title")

使用 icon 图标文字
<i class="icon-cog"></i>

段落：以一个空行开始，以一个空行结束，中间的就是一个段落。

表格：

Item     | Value
-------- | ---
Computer | $1600
Phone    | $12
Pipe     | $1

无序列表：使用 - 加一个空格（）

- 无需列表1
- 无序列表2
- 无序列表3

有序列表：使用 数字 加一个英文句点

1. 有序列表
2. 有序列表
3. 有序列表
4. 有序列表
5. 有序列表

换行缩进形成代码区块

    这里先换行，然后缩进4个空格，之后的内容便可以原样显示了，适合用于显示代码内容。直到文本结束或最后一个存在缩进的行为止。

块引用
>给引用的文本开始位置都加一个 '>'，
>便可组成一个块引用。在块引用中，可以结合
>其他markdown元素一块使用，比如列表。
>**强调**
也可以只在第一行加大于号，其他位置不加。

>- 块引用里使用列表，需要和上面的内容隔开一个空行
>- 记得加空格哦。
