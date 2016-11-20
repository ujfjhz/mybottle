% rebase('base.tpl', title='Query page')
<script>
$(document).ready(function(){
dtJson={
        dom: 'Blfrtip',
	buttons:[
	{
            extend: 'excelFlash',
            text: '下载为Excel',
            exportOptions: {
                modifier: {
                    search: 'none'
                }
            }
        }],
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
<form id="queryform" method="POST" action="/query" class="border">
    <p><label class="field"> title:</label> <input name="title" type="text" />
    <label class="field"> content:</label> <input name="content" type="text" />
    <label class="field"> column1:</label> <input name="column1" type="text" /></p>
    <p><label class="field"> column2:</label> <input name="column2" type="text" />
    <label class="field"> column3:</label> <input name="column3" type="text" />
    <input value="Query" type="submit" /></p>
</form>

<button id="insertbt" type="button" class="right">insert</button>
<div class="center" > 查询结果如下 </div>
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

