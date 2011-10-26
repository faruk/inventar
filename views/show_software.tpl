%# template for the form for a new hardware part

<h1>edit software</h1>
<form action = "/software/{{software['id']}}" method = "GET">
<table border = "1">
  <tr>
    <td>name:</td>
    <td><input type="text" size = "50" maxlength = "100" name="name" value="{{software['name']}}"></td>
  </tr>
  <tr>
    <td>license key:</td>
    <td><input type="text" size = "50" maxlength = "100" name="license_key" value="{{software['license_key']}}"></td>
  </tr>
  <tr>
    <td>buying date:</td>
    <td><input type="text" size = "50" maxlength = "100" name="buying_date" value="{{software['buying_date']}}"></td>
  </tr>
  <tr>
    <td>billing number:</td>
    <td><input type="text" size = "50" maxlength = "100" name="billing_number" value="{{software['billing_number']}}"></td>
  </tr>
  <tr>
    <td>department</td>
    <td>
      <select name = "department">
        <option>{{software['department']}}</option>
        %for department in departments:
        <option>{{department['name']}}</option>
        %end
      </select>
    </td>
  </tr>
  <tr>
    <td>other:</td>
    <td><textarea cols = "50" rows = "3" name="other">{{software['other']}}</textarea></td>
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
