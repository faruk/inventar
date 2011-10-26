%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<h1>users</h1>
<table border="1">
  <tr>
    <th>first name</th>
    <th>last name</th>
    <th>room</th>
    <th>telephone</th>
  </tr>
  %for row in rows:
  <tr>
    <td>{{row['first_name']}}</td>
    <td>{{row['last_name']}}</td>
    <td>{{row['room']}}</td>
    <td>{{row['telephone']}}</td>
    <td>{{row['department']}}</td>
    <td><a href = "/user/{{row['id']}}">show & edit</a></td>
    <td><a href = "/user/delete/{{row['id']}}">delete</a></td>
  </tr>
  %end
</table>
%rebase main content = False
