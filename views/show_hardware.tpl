%# template for the form for a new hardware part

<h1>edit hardware:</h1>
<form action = "/hardware/{{id}}" method = "GET">
<table border = "1">
  <tr>
    <td>serial no:</td>
    <td><input type="text" size = "50" maxlength = "100" name="serial_number" value="{{row['serial_number']}}"></td>
  </tr>
  <tr>
    <td>sap no:</td>
    <td><input type="text" size = "50" maxlength = "100" name="sap_number" value="{{row['sap_number']}}"></td>
  </tr>
  <tr>
    <td>zedat no:</td>
    <td><input type="text" size = "50" maxlength = "100" name="zedat_number" value="{{row['zedat_number']}}"></td>
  </tr>
  <tr>
    <td>billing no:</td>
    <td><input type="text" size = "50" maxlength = "100" name="billing_no" value="{{row['billing_number']}}"></td>
  </tr>
  <tr>
    <td>buying date:</td>
    <td><input type="text" size = "50" id="datepicker" name="buying_date"></td>
  </tr>
  <tr>
    <td>article no:</td>
    <td><input type="text" size = "50" maxlength = "100" name ="article_number" value="{{row['article_number']}}"></td>
  </tr>
  <tr>
    <td>room no:</td>
    <td><select name="room">
      <option>{{row['room']}}</option>
      %for room in rooms:
      <option>{{room['number']}}</option>
      %end
    </td>
  </tr>
  <tr>
    <td>socket:</td>
    <td><select name="socket">
      <option>{{row['socket']}}</option>
      %for socket in sockets:
      <option>{{socket['number']}}</option>
      %end
    </td>
  </tr> 
  <tr>
    <td>department:</td>
    <td><select name="room">
      <option>{{row['department']}}</option>
      %for department in departments:
      <option>{{department['name']}}</option>
      %end
    </td>
  </tr>
  <tr>
    <td>description:</td><td><textarea name = "description" rows="3" cols="50" maxlength = "255"></textarea></td>
  </tr>
  <tr>
    <td>other:</td><td><textarea name="other" rows="3" cols="50" maxlength="255"></textarea></td>
  </tr>
  <tr>
    <td><input type="submit" name="save"></td><td></td>
  </tr>
</table>

<script type="text/javascript">
  //$(document).ready(function() {
  //  $(function() {
  //    $( "#datepicker" ).datepicker();
  //  });
  //});
</script>

%rebase main content = False
