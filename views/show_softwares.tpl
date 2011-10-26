%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<h1>software</h1>
<table border="1">
  <tr>
    <th>name</th>
    <th>license key</th>
    <th>buying date</th>
    <th>billing number</th>
    <th>other</th>
  </tr>
  %for row in rows:
  <tr>
    <td>{{row['name']}}</td>
    <td>{{row['license_key']}}</td>
    <td>{{row['buying_date']}}</td>
    <td>{{row['billing_number']}}</td>
    <td>{{row['department']}}</td>
    <td><a href = "/software/{{row['id']}}">show & edit</a></td>
    <td><a href = "/software/delete/{{row['id']}}">delete</a></td>
  </tr>
  %end
</table>
%rebase main content = False
