<table class="table">
    <thead>
        <tr>
            <th>name</th>
            <th>sap</th>
            <th>zedat</th>
            <th>oei</th>
            <th>barcode</th>
            <th>buyed</th>
            <th>notes</th>
            <th>room</th>
            <th>department</th>
            <th>actions</th>
        </tr>
    </thead>
    <tbody>
        %for hardware in hardwares:
        <tr>
            <td>{{hardware[1]}}</td>
            <td>{{hardware[2]}}</td>
            <td>{{hardware[3]}}</td>
            <td>{{hardware[4]}}</td>
            <td>{{hardware[5]}}</td>
            <td>{{hardware[6]}}</td>
            <td>{{hardware[7]}}</td>
            <td>{{hardware[8]}}</td>
            <td>{{hardware[9]}}</td>
            <td>
                <a href="/hardware/edit/{{hardware[0]}}" class="btn btn-primary inline">edit</a>
                <a href="/hardware/delete/{{hardware[0]}}" class="btn btn-warning inline">delete</a></td>
        </tr>
        %end
    </tbody>
</table>

%rebase index
