% include('header.tpl')
<form action="/insert" method="post">
请输入：
    <p><label class="field"> Text:</label> <input name="title" type="text" /></p>
    <p><label class="field"> Content:</label> <input name="content" type="text" /></p>
    <p><input value="insert" type="submit" /></p>
</form>
% include('footer.tpl') 
