%# template for the form for a new hardware part

<h1>Add new Room to the Database:</h1>
<form action = "/room/new" method = "GET">
<table border = "1">
  <tr>
    <td>number:</td><td><input type="text" size = "50" maxlength = "100" name="number"></td>
  </tr>
  <tr>
    <td>department</td>
    <td>
      <select name = "department">
        <option></option>
        %for department in departments:
        <option>{{department['name']}}</option>
        %end
      </select>
    </td>
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
