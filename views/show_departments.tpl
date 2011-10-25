%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<h1>{{name}}</h1>
<table border="1">
  <tr>
    <th>name</th>
  </tr>
  %for row in rows:
  <tr>
    <td>{{row[0]}}</td>
    <td><a href = "/department/edit/{{row[1]}}">show & edit</a></td>
    <td><a href = "/department/delete/{{row[1]}}">delete</a></td>
  </tr>
  %end
</table>
%rebase main content = False
