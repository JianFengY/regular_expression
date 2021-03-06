## 正则表达式语法

字符|匹配
:---:|:---:
.|匹配任意字符，除了\n
[...]|匹配字符集内任一字符
\d|匹配数字
\D|匹配非数字
\s|匹配空白
\S|匹配非空白字符
\w|匹配单词字符```[a-zA-Z0-9]```
\W|匹配非单词字符
*|匹配前一个字符任意次
+|匹配前一个字符至少一次
?|匹配前一个字符0或1次
{m}|匹配前一个字符m次
{m,}|匹配至少m次
{m,n}|匹配前一个字符m到n次
^|匹配字符串起始部分,```^\d```表示必须以数字开头
$|匹配字符串终止部分,```\d$```表示必须以数字结束
*?或+?或??|匹配模式变为非贪婪（尽可能少匹配字符）
\A或\Z|指定字符串必须出现在开头/结尾
｜|匹配左边或右边任意一个
()|括号中的表达式作为一个分组
\<number>|引用编号为number的分组匹配到的字符串
(?P<name>)|分组起一个别名
(?P=name)|引用别名为name的分组匹配字符串

以下式中"^"就是限定开头的意思:
```
/[(^\s+)(\s+$)]/g
(^cat)$
(^cat$)
^(cat)$
^(cat$)
```
以下式中"^"表示的就是表示字符类的否定：
```
[^a]表示“匹配除了a的任意字符”。
[^a-zA-Z0-9]表示“找到一个非字母也非数字的字符”。
[\^abc]表示“找到一个插入符或者a或者b或者c”。
[^\^]表示“找到除了插入符外的任意字符”。
```