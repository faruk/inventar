<form class="well form-horizontal">
    <fieldset>
        <legend>New Software</legend>
        <div class="control-group">
            <label class="control-label" for="name">Name</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="name" name="name" value="{{software[1]}}">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="sap">SAP-No.</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="sap" name="sap" value="{{software[2]}}">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="zedat">Zedat-No.</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="zedat" name="zedat" value="{{software[3]}}">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="oei">OEI-No.</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="oei" name="oei" value="{{software[4]}}">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="barcode">Barcode</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="barcode" name="barcode" value="{{software[5]}}">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="license">License</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="license" name="license" value="{{software[6]}}">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="buying_date">Buying Date</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="buying_date" name="buying_date" value="{{software[7]}}">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="notes">Notes</label>
            <div class="controls">
                <textarea class="input-xlarge" name="notes" id="notes" rows="3">{{software[8]}}</textarea>
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="id_department">Department</label>
            <div class="controls">
                <select class="input-xlarge" name="id_department" id="id_department">
                    <option value="{{software[9]}}">{{software[10]}}</option>
                    %for department in departments:
                    <option value="{{department[0]}}">{{department[1]}}</option>
                    %end
                </select>
            </div>
        </div>
        <div class="form-actions">
            <input type="hidden" name="id" value="{{software[0]}}">
            <input type="submit" name="save" class="btn btn-primary">
            <a href="/software/all" class="btn btn-warning">cancel</a>
        </div>
    </fieldset>
</form>

%rebase index
