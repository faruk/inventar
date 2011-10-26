%# template for the form for a new hardware part

<h1>edit room</h1>
<form action = "/room/{{room['id']}}" method = "GET">
<table border = "1">
  <tr>
    <td>number:</td>
    <td><input type="text" size = "50" maxlength = "100" name="number" value = "{{room['number']}}"></td>
  </tr>
  <tr>
    <td>department</td>
    <td>
      <select name = "department">
        <option>{{room['department']}}</option>
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
