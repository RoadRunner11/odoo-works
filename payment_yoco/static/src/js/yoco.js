odoo.define('payment_stripe.stripe', function (require) {
    "use strict";
    
    var ajax = require('web.ajax');
    var core = require('web.core');
    
    var qweb = core.qweb;
    var _t = core._t;

    ajax.loadXML('/payment_yoco/static/src/xml/yoco_templates.xml', qweb);
    
    if ($.blockUI) {
        // our message needs to appear above the modal dialog
        $.blockUI.defaults.baseZ = 2147483647; //same z-index as Rave Checkout
        $.blockUI.defaults.css.border = '0';
        $.blockUI.defaults.css["background-color"] = '';
        $.blockUI.defaults.overlayCSS["opacity"] = '0.9';
    }
    var observer = new MutationObserver(function (mutations, observer) {
        for (var i = 0; i < mutations.length; ++i) {
            for (var j = 0; j < mutations[i].addedNodes.length; ++j) {
                if (mutations[i].addedNodes[j].tagName.toLowerCase() === "form" && mutations[i].addedNodes[j].getAttribute('provider') === 'yoco') {
                    display_yoco_form($(mutations[i].addedNodes[j]));
                }
            }
        }
    });
    
    function displayError(message) {
        var wizard = $(qweb.render('yoco.error', {'msg': message || _t('Payment error')}));
        wizard.appendTo($('body')).modal({'keyboard': true});
        if ($.blockUI) {
            $.unblockUI();
        }
        $("#o_payment_form_pay").removeAttr('disabled');
    }

    require('web.dom_ready');
    if (!$('.o_payment_form').length) {
        return Promise.reject("DOM doesn't contain '.o_payment_form'");
    }else{
    
        function display_yoco_form(provider_form){
            // Open Checkout with further options
            if ($.blockUI) {
                var msg = _t("Just one more second, We are redirecting you to Yoco...");
                $.blockUI({
                    'message': '<h2 class="text-white"><img src="/web/static/src/img/spin.png" class="fa-pulse"/>' +
                            '    <br />' + msg +
                            '</h2>'
                });
            }

            var yoco = new window.YocoSDK({
                publicKey: 'pk_test_ed3c54a6gOol69qa7f45',
              });
        }

        $.getScript("https://js.yoco.com/sdk/v1/yoco-sdk-web.js", function(data, textStatus, jqxhr) {
            display_yoco_form($('form[provider="yoco"]'));
        });
    };
})