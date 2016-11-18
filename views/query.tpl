% include('header.tpl')
<form action="/query" method="post">
    title: <input name="title" type="text" />
    <input value="Query" type="submit" />
</form>

<br>
<a href="/insert" target="view_window">insert</a>

%if title:
title: {{title}}
%end
%if content:
content: {{content}}
%end
% include('footer.tpl') 
