'use strict';

class ItemsTable extends HTMLElement {

    constructor() {
        const self = super();

        const bulma = document.createElement("link");
        bulma.setAttribute('rel', 'stylesheet');
        bulma.setAttribute('href', 'https://cdn.jsdelivr.net/npm/bulma@0.8.2/css/bulma.min.css');

        const style = document.createElement("link");
        style.setAttribute('rel', 'stylesheet');
        style.setAttribute('href', '/static/css/inventory/items.table.css');

        const div = document.createElement('div');
        div.classList.add('component-wrapper');

        this.init(self, div);

        const shadow = this.attachShadow({ mode: 'open' });
        shadow.appendChild(bulma);
        shadow.appendChild(style);
        shadow.appendChild(div);

        this.setItems = this.setItems.bind(this);
    }

    init(component, container) {
        const ths = [];
        ths.push(`<th class="col-select"></th>`);
        ths.push(`<th class="col-name"><span>Name</span></th>`);
        ths.push(`<th class="col-description"><span>Description</span></th>`);
        const thall = ths.join('');

        const div = document.createElement('div');
        div.classList.add('wrapper');
        div.innerHTML = `
            <div class="table-wrapper">
                <table class="tbl-items">
                    <caption>Items</caption>
                    <colgroup>
                        <col class="col-select">
                        <col class="col-name">
                        <col class="col-description">
                    </colgroup>
                    <thead>
                        ${thall}
                    </thead>
                    <tbody>
                    </tbody>
                    <tfoot>
                    </tfoot>
                </table>
            </div><!-- .table-wrapper -->
        `;


        container.appendChild(div);
    }

    setItems(items = [], filter = '') {
        const self = this;
        const shadow = this.shadowRoot;

        const tbody = shadow.querySelector('table.tbl-items tbody');
        while(tbody.firstChild) {
            tbody.removeChild(tbody.lastChild);
        }

        items.forEach(item => {
            const tds = [];
            tds.push(`<td class="col-select"><input type="radio" id="id${item.id}" name="selected" title="Select Item" value="${item.id}" /></td>`);
            tds.push(`<td class="col-name"><span>${item.name}</span></td>`);
            tds.push(`<td class="col-description">${item.description}</td>`);
            const tdall = tds.join('');

            const tr = document.createElement('tr');
            tr.classList.add('row-item');
            tr.innerHTML = `
                ${tdall}
            `;

            tbody.appendChild(tr);
        });
    }
}
customElements.define('items-table', ItemsTable);
export { ItemsTable };