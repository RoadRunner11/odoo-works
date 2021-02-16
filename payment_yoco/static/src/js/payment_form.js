odoo.define('payment_yoco.payment_form', function (require) {
    "use strict";
    
    var ajax = require('web.ajax');
    var core = require('web.core');
    var Dialog = require('web.Dialog');
    var PaymentForm = require('payment.payment_form');

    var qweb = core.qweb;
    var _t = core._t;

    ajax.loadXML('/yoco_payments_acquirer/static/src/xml/yoco_templates.xml', qweb);
    
    if ($.blockUI) {
        // our message needs to appear above the modal dialog
        $.blockUI.defaults.baseZ = 2147483647; //same z-index as Rave Checkout
        $.blockUI.defaults.css.border = '0';
        $.blockUI.defaults.css["background-color"] = '';
        $.blockUI.defaults.overlayCSS["opacity"] = '0.9';
    }
    PaymentForm.include({

        willStart: function () {
            return this._super.apply(this, arguments).then(function () {
                return ajax.loadJS("https://js.stripe.com/v3/");
            })
        },

    })    

})