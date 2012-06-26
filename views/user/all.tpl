<table class="table">
    <thead>
        <tr>
            <th>forename</th>
            <th>lastname</th>
            <th>username</th>
            <th>department</th>
        <tr>
    </thead>
    <tbody>
        %for user in users:
        <tr>
            <td>{{user[1]}}</td>
            <td>{{user[2]}}</td>
            <td>{{user[3]}}</td>
            <td>{{user[4]}}</td>
            <td><a href="/user/edit/{{user[0]}}" class="btn btn-primary">edit</a></td>
            <td><a href="/user/delete/{{user[0]}}" class="btn btn-warning">delete</a></td>
        </tr>
        %end
    </tbody>
</table>

%rebase index
