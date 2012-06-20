<form class="well form-horizontal" action="/department/new" method="GET">
    <fieldset>
        <legend>New Department</legend>
        <div class="control-group">
            <label class="control-label" for="name">Name</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="name" name="name">
            </div>
        </div>
        <div class="form-actions">
            <input type="submit" name="save" class="btn btn-primary">
            <a href="/department/all" class="btn btn-warning">cancel</a>
        </div>
    </fieldset>
</form>

%rebase index
