odoo.define('odoo_owl_v15.vehicle_popup', function(require){
    'use strict';

    var FormController = require('web.FormController');

    var ExtendFormController = FormController.include({
    saveRecord: function(){
        var dataSave = this._super.apply(this,arguments);
        console.log(dataSave);
        if(this.modelName === 'vehicle'){
            self = this;
            self._rpc({
                        model: 'vehicle',
                        method: 'search_read',
                        fields: ['car_name'],
                        domain: [['id','=',self.model.__id]],
                        context: self.context,
                        }).then(function(result){
                            console.log(result,'is the resultr');
                        });
           self.displayNotification({
           type: 'warning',
           title: 'Success',
           message: "Record Saved successfully...!",
           sticky: false
            });

        }

        return dataSave;
    }
    });
});