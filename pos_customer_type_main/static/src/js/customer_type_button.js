/**@odoo-module **/
import { _t } from "@web/core/l10n/translation";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { CustomerTypePopup } from "pos_customer_type_main.CustomerTypePopup";

export class CustomerTypeButton extends Component {
	
    static template = "CustomerTypeButton";
	
    /** 
    * Setup function to initialize the component.
    */
    setup() {    
        this.pos = usePos();
        this.popup = useService("popup");
    }
	
    /** 
    * Click event handler for the Customer Type button.
    */
    async onClick() {    
        this.popup.add(CustomerTypePopup, {
            title: _t('Select Customer Type'),
            body: _t('Choose a customer type from the list')
        });
    }
}
console.log("Adding CustomerTypeButton to ProductScreen");
/**
 * Add the CustomerTypeButton component to the control buttons in
 * the ProductScreen.
 */
ProductScreen.addControlButton({
    component: CustomerTypeButton,
    condition: function () {
        return this.env.pos;
    },
});
