%# template for the form for a new hardware part

<h1>edit department:</h1>
<form action = "/department/{{id}}" method = "GET">
<table border = "1">
  <tr>
    <td>name:</td><td><input type="text" size = "50" maxlength = "100" name="name" value="{{row['name']}}"></td>
  </tr>
  <tr>
    <td><input type="submit" name="save"></td><td></td>
  </tr>

</table>
</form>

<script type="text/javascript">
  //$(document).ready(function() {
  //  $(function() {
  //    $( "#datepicker" ).datepicker();
  //  });
  //});
</script>

%rebase main content = False
