% include('header.tpl')
<form action="/login" method="post">
    <p><label class="field"> Username:</label> <input name="username" type="text" /></p>
    <p><label class="field"> Password:</label> <input name="password" type="password" /></p>
    <p><input value="Login" type="submit" /></p>
</form>
% include('footer.tpl') 
