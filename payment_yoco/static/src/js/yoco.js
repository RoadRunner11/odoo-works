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

    require('web.dom_ready');
    if (!$('.o_payment_form').length) {
        return Promise.reject("DOM doesn't contain '.o_payment_form'");
    }

    var observer = new MutationObserver(function (mutations, observer) {
        for (var i = 0; i < mutations.length; ++i) {
            for (var j = 0; j < mutations[i].addedNodes.length; ++j) {
                console.log(mutations[i].addedNodes)
                console.log(mutations[i].addedNodes.length)
                console.log(mutations[i].addedNodes.tagName)
                // if (mutations[i].addedNodes[j].tagName.toLowerCase() === "form" && mutations[i].addedNodes[j].getAttribute('provider') === 'yoco') {
                display_yoco_form($(mutations[i].addedNodes[j]));
                // }
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
        var paymentForm = $('.o_payment_form');
        if (!paymentForm.find('i').length) {
            paymentForm.append('<i class="fa fa-spinner fa-spin"/>');
            paymentForm.attr('disabled', 'disabled');
        }

        var _getYocoInputValue = function (name) {
            return provider_form.find('input[name="' + name + '"]').val();
        };

        var yoco = new window.YocoSDK({
            publicKey: _getYocoInputValue('yoco_pub_key'),
            });

        yoco.showPopup({
            amountInCents: 2799,
            currency: 'ZAR',
            name: 'Your Store or Product',
            description: 'Awesome description',
            callback: function (result) {
                // This function returns a token that your server can use to capture a payment
                if (result.error) {
                const errorMessage = result.error.message;
                alert("error occured: " + errorMessage);
                } else {
                alert("card successfully tokenised: " + result.id);
                }
                // In a real integration - you would now pass this chargeToken back to your
                // server along with the order/basket that the customer has purchased.
            }
        })
    }

    $.getScript("https://js.yoco.com/sdk/v1/yoco-sdk-web.js", function(data, textStatus, jqxhr) {
        observer.observe(document.body, {childList: true});
        display_yoco_form($('form[provider="yoco"]'));
    });
    
})