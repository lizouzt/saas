'use strict';
import { notify } from '/static/js/ui/ui.js';
import { Accounts } from '/static/js/modules/accounting/accounts.js';
import { Util } from '/static/js/util.js';
class AccountEditor extends HTMLElement {

    constructor() {
        const self = super();

        const style = document.createElement("link");
        style.setAttribute('rel', 'stylesheet');
        style.setAttribute('href', '/static/custom-elements/accounting/account-editor/account-editor.css');

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

        this._getClientId = this._getClientId.bind(this);
        this._attachEventHandlers = this._attachEventHandlers.bind(this);

        this._attachEventHandlers();
    }

    _init(container) {
        const client_id = this.getAttribute("client-id");

        const div = document.createElement('div');
        div.classList.add('wrapper');
        div.innerHTML = `
            <div class="toolbar" role="toolbar">
                <button type="button" class="btn btn-save" title="Save">
                    <span class="material-icons">save</span>
                </button>
            </div><!-- .toolbar -->
            <div class="form-wrapper">
                <form class="form-account-editor">
                    <input type="hidden" id="client-id" name="client_id" title="Name" placeholder="Name" value="${client_id}" />

                    <!-- type -->
                    <label for="type">Type</label>
                    <select id="type" name="type" class="form-input-select" title="Type">
                    </select>

                    <!-- name -->
                    <label for="name">Name</label>
                    <input type="text" id="name" name="name" class="form-input-text" />

                    <!-- description -->
                    <label for="description">Description</label>
                    <textarea id="description" name="description" class="form-input-textarea" title="Description"></textarea>
                </form>
            </div><!-- .form-wrapper -->
        `;

        container.appendChild(div);

        Accounts.getAccountTypes().then((r) => {
            if (r.status == 'success') {
                const types = r.json.types;
                const options = [];
                types.forEach((type) => {
                    options.push(`<option value="${type.id}">${type.name}</option>`);
                });
                const select = div.querySelector('#type');
                select.innerHTML = options.join('');
            } else {
                notify(r.status, r.message);
            }
         });
    }

    _getClientId() {
        const shadow = this.shadowRoot;
        const client = shadow.getElementById('client-id');
        return client.value;
    }

    _attachEventHandlers() {
        const self = this;
        const shadow = this.shadowRoot;

        const client_id = this._getClientId();
        const account_id = this.getAttribute('account-id');

        const btnsave = shadow.querySelector('button.btn-save');
        btnsave.addEventListener('click', function(e) {
            const type = shadow.getElementById('type');
            const name = shadow.getElementById('name');
            const description = shadow.getElementById('description');

            if (account_id) {
                Accounts.update(client_id, account_id, type.value, name.value, description.value).then((r) => {
                    notify(r.status, r.message, 3000);
                });
            } else {
                const tmp_account_id = Util.generateUUID();
                Accounts.add(client_id, tmp_account_id, type.value, name.value, description.value).then((r) => {
                    notify(r.status, r.message, 3000);
                });
            }
            e.preventDefault();
        });
    }
}
customElements.define('account-editor', AccountEditor);
export { AccountEditor };