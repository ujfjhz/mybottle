% rebase('base.tpl', title='Login page')
<form action="/login" method="post" class="border center">
    <p><label class="field"> Username:</label> <input name="username" type="text" /></p>
    <p><label class="field"> Password:</label> <input name="password" type="password" /></p>
    <p><input value="Login" type="submit" /></p>
    <p> 登陆失败，请重新登陆</p>
</form>
