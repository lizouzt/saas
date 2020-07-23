'use strict';
import { notify, showInView } from '/static/js/ui/ui.js';
class AccountSelector extends HTMLElement {

    constructor() {
        const self = super();

        const style = document.createElement("link");
        style.setAttribute('rel', 'stylesheet');
        style.setAttribute('href', '/static/custom-elements/accounting/account-selector/account-selector.css');

        const default_style = document.createElement("link");
        default_style.setAttribute('rel', 'stylesheet');
        default_style.setAttribute('href', '/static/css/default.css');

        const div = document.createElement('div');
        div.classList.add('component-wrapper');

        this._init(div);

        const shadow = this.attachShadow({ mode: 'open' });
        shadow.appendChild(style);
        shadow.appendChild(default_style);
        shadow.appendChild(div);

        this._attachEventHandlers = this._attachEventHandlers.bind(this);
        this.value = this.value.bind(this);

        this._attachEventHandlers();
    }

    static get observedAttributes() { 
        return ['account-id']; 
    }

    attributeChangedCallback(name, oldValue, newValue) {
        if (name == 'account-id') {
            self._account_id = this.getAttribute('account-id');
        }
    }

    _init(container) {
        const div = document.createElement('div');
        div.classList.add('wrapper');
        div.innerHTML = `
            <input type="text" id="display" name="display" class="form-input-display" title="Select Account" placeholder="Account" readonly />
            <button type="button" id="btn-select" class="btn btn-select" title="Select">&hellip;</button>
        `;

        container.appendChild(div);
    }

    _attachEventHandlers() {
        const self = this;
        const shadow = this.shadowRoot;

        const client_id = this.getAttribute('client-id');

        const input_display = shadow.getElementById('display');

        const btnselect = shadow.getElementById('btn-select');
        btnselect.addEventListener('click', function() {
            const selector = showInView('Select Account', `<account-selector-view client-id="${client_id}"></account-selector-view>`);
            selector.addEventListener('selected', function(e) {
                const account = e.detail.account;

                input_display.value = account.name;
                self.setAttribute('account-id', account.id);
            });
        });
    }

    value() {
        const self = this;
        return self._account_id;
    }
}
customElements.define('account-selector', AccountSelector);