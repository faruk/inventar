%# template for the form for a new hardware part

<h1>Add new User to the Database:</h1>
<form action = "/user/{{user['id']}}" method = "GET">
<table border = "1">
  <tr>
    <td>first name:</td>
    <td><input type="text" size = "50" maxlength = "100" name="first_name" value="{{user['first_name']}}"></td>
  </tr>
  <tr>
    <td>last name:</td>
    <td><input type="text" size = "50" maxlength = "100" name="last_name" value="{{user['last_name']}}"></td>
  </tr>
  <tr>
    <td>room:</td>
    <td>
      <select name = "room">
        <option>{{user['room']}}</option>
        %for room in rooms:
        <option>{{room['number']}}</option>
        %end
      </select>
    </td>
  </tr>
  <tr>
    <td>department</td>
    <td>
      <select name = "department">
        <option>{{user['department']}}</option>
        %for department in departments:
        <option>{{department['name']}}</option>
        %end
      </select>
    </td>
  </tr>
  <tr>
    <td>telephone:</td><td><input type="text" size = "50" maxlength = "100" name="telephone"></td>
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
