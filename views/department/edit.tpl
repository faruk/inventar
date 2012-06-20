<form class="well form-horizontal" action="/department/edit/{{department[0]}}" method="GET">
    <fieldset>
        <legend>Edit Department</legend>
        <div class="control-group">
            <label class="control-label" for="name">Name</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="name" name="name" value="{{department[1]}}">
            </div>
        </div>
        <div class="form-actions">
            <input type="hidden" name="id" value="{{department[0]}}">
            <input type="submit" name="save" class="btn btn-primary">
            <a href="/department/all" class="btn btn-warning">cancel</a>
        </div>
    </fieldset>
</form>

%rebase index
