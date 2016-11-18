% include('header.tpl')
<form action="/insert" method="post">
    Text: <input name="title" type="text" />
    Content: <input name="content" type="text" />
    <input value="insert" type="submit" />
</form>
% include('footer.tpl') 
