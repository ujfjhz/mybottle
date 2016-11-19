% rebase('base.tpl', title='Query page')
<script>
$(document).ready(function(){
dtJson={
        destroy: true,
	searching: false,
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": $("#queryform").attr("action"),
	    "data": function(d){
	       var frm_data = $('#queryform').serializeArray();
	       $.each(frm_data, function(key, val) {
		 d[val.name] = val.value;
	       });

	    },
            "type": "POST"
        },
        "columns": [
            { "data": "id" },
            { "data": "title" },
            { "data": "content" }
        ]
    }
$('#example').DataTable(dtJson);

$("#queryform").submit(function(event){
    event.preventDefault();
    $('#example').DataTable(dtJson);
});

$("#insertbt").click(function(){
window.open('/insert', '_blank').focus();
}
);

}
)
</script>
<form id="queryform" method="POST" action="/query">
    title: <input name="title" type="text" />
    <input value="Query" type="submit" />
</form>
<br>
<button id="insertbt" type="button">insert</button>
<hr>
<p> the results  is:</p>
<table id="example" class="display" cellspacing="0" width="100%">
        <thead>
            <tr>
                <th>Id</th>
                <th>Title</th>
                <th>Content</th>
            </tr>
        </thead>
        <tfoot>
            <tr>
                <th>Id</th>
                <th>Title</th>
                <th>Content</th>
            </tr>
        </tfoot>
</table>

<br>

