
var ROW_NUMBER = 5;

Date.prototype.addDays = function(days) {
    var date = new Date(this.valueOf());
    date.setDate(date.getDate() + days);
    return date;
}


$(document).ready( function () {

    /* create datepicker */
    $("#txt_OrderDate").datepicker({ 
        dateFormat: 'dd/mm/yy' 
    });
    
    $('#btn_OrderDate').click(function() {
        $('#txt_OrderDate').datepicker('show');
    });

    $("#txt_Date").datepicker({ 
        dateFormat: 'dd/mm/yy' 
    });
    
    $('#btn_Date').click(function() {
        $('#txt_Date').datepicker('show');
    });

    /* table add delete row */
    var $TABLE = $('#div_table');
    $('.table-add').click(function () {
        var $clone = $TABLE.find('tr.hide').clone(true).removeClass('hide table-line');
        $TABLE.find('tbody').append($clone);
        re_order_no();
    });

    $('.table-remove').click(function () {
        $(this).parents('tr').detach();

        if ($('#table_main tr').length <= 9) {
            $('.table-add').click();
        }
        re_order_no();
        re_calculate_total_price();
    });

    $('#txt_IdUser').change (function () {
        var id_user = $(this).val().trim();

        $.ajax({
            url:  '/customer/detail/' + id_user,
            type:  'get',
            dataType:  'json',
            success: function  (data) {
                $('#txt_IdUser').val(data.customers.id_user);
                $('#txt_Username').val(data.customers.username);
            },
            error: function (xhr, status, error) {
                $('#txt_Username').val('');
            }
        });
    });

    $('#txt_PaymentMethod').change (function () {
        var payment_method = $(this).val().trim();

        $.ajax({
            url:  '/paymentmethod/detail/' + payment_method,
            type:  'get',
            dataType:  'json',
            success: function  (data) {
                $('#txt_PaymentMethod').val(data.payment_methods.payment_method);
                $('#txt_Description').val(data.payment_methods.description);
            },
            error: function (xhr, status, error) {
                $('#txt_Description').val('');
            }
        });
    });

    $('#txt_Menu').change (function () {
        var menu_id = $(this).val().trim();

        $.ajax({
            url:  '/menu/detail/' + menu_id,
            type:  'get',
            dataType:  'json',
            success: function  (data) {
                $('#txt_Menu').val(data.menu.menu_id);
                $('#txt_MenuName').val(data.menu.menu_name);
                $('#txt_MenuPrice').val(data.menu.price);
            },
            error: function (xhr, status, error) {
                $('#txt_MenuName').val('');
                $('#txt_MenuPrice').val('');
            }
        });
    });


// ================================================================================
   /* search type */
$('.search_product_code').click(function () {
    $(this).parents('tr').find('.order_no').html('*');  // mark row number with '*' for return value after close modal

    $.ajax({                                        // call backend /product/list
        url:  '/product/list',
        type:  'get',
        dataType:  'json',
        success: function  (data) {
            let rows =  '';
            var i = 1;
            data.products.forEach(product => {       // loop each result of products to create table rows
                rows += `
                <tr>
                    <td>${i++}</td>
                    <td><a class='a_click' href='#'>${product.code}</a></td>
                    <td>${product.name}</td>
                    <td>${formatNumber(product.units)}</td>
                    <td class='hide'></td>
                </tr>`;
            });
            $('#table_modal > tbody').html(rows);       // set new table rows to table body (tbody) of popup

            $('#model_header_1').text('Product Code');      // set header of popup
            $('#model_header_2').text('Product Name');
            $('#model_header_3').text('Unit Price');

            
            $('#txt_modal_param').val('product_code');      // mark product_code for check after close modal
            $('#modal_form').modal();                       // open popup
        },
    });
});

    /* search additional items */
    $('.search_additional_items').click(function () {
        $(this).parents('tr').find('.additional_items_1').html('*');
        $.ajax({
            url:  '/additional_items/list',
            type:  'get',
            dataType:  'json',
            success: function  (data) {
                let rows =  '';
                var i = 1;
                data.additionalitems.forEach(additionalitem => {
                    rows += `
                    <tr class="d-flex">
                        <td class='col-1'>${i++}</td>
                        <td class='col-3'><a class='a_click' href='#'>${additionalitem.type}</a></td>
                        <td class='col-5'>${additionalitem.description}</td>
                        <td class='col-3'>${additionalitem.mash}</td>
                        <td class='hide'></td>
                    </tr>`;
                });
                $('#table_modal > tbody').html(rows);

                $('#model_header_1').text('Type');
                $('#model_header_2').text('Description');
                $('#model_header_3').text('Mash');

            },
        });        
        // open popup
        $('#txt_modal_param').val('type');
        $('#modal_form').modal();
    });

    /* search sweet level */
    $('.search_sweet_level').click(function () {
        $(this).parents('tr').find('.sweet_1').html('*');
        $.ajax({
            url:  '/sweet/list',
            type:  'get',
            dataType:  'json',
            success: function  (data) {
                let rows =  '';
                var i = 1;
                data.sweets.forEach(sweet => {
                    rows += `
                    <tr class="d-flex">
                        <td class='col-1'>${i++}</td>
                        <td class='col-3'><a class='a_click' href='#'>${sweet.sweet_level}</a></td>
                        <td class='col-5'>${sweet.description}</td>
                        <td class='col-3'></td>
                        <td class='hide'></td>
                    </tr>`;
                });
                $('#table_modal > tbody').html(rows);

                $('#model_header_1').text('Sweet Level');
                $('#model_header_2').text('Description');
                $('#model_header_3').text('Note');

            },
        });        
        // open popup
        $('#txt_modal_param').val('sweet_level');
        $('#modal_form').modal();
    });

        /* search menu code  */
    $('.search_menu_id').click(function () {
        $(this).parents('tr').find('.order_no').html('*');
        
        $.ajax({
            url:  '/menu/list',
            type:  'get',
            dataType:  'json',
            success: function  (data) {
                let rows =  '';
                var i = 1;
                data.menus.forEach(menu => {
                    rows += `
                    <tr class="d-flex">
                        <td class='col-1'>${i++}</td>
                        <td class='col-3'><a class='a_click' href='#'>${menu.menu_id}</a></td>
                        <td class='col-5'>${menu.menu_name}</td>
                        <td class='col-3'>${formatNumber(menu.price)}</td>
                        <td class='hide'></td>
                    </tr>`;
                });
                $('#table_modal > tbody').html(rows);

                $('#model_header_1').text('Menu Code');
                $('#model_header_2').text('Menu Name');
                $('#model_header_3').text('Unit Price');
                // $('#model_header_3').text('Note');

            },
        });        
        // open popup
        $('#txt_modal_param').val('menu_id');
        $('#modal_form').modal();
    });

    // After click link in Model (popup), Return value of product_code, customer_code, invoice_no to main form
    $('body').on('click', 'a.a_click', function() {
        var code = $(this).parents('tr').find('td:nth-child(2)').children().html();
        var name = $(this).parents('tr').find('td:nth-child(3)').html();
        var note = $(this).parents('tr').find('td:nth-child(4)').html();
        var option = $(this).parents('tr').find('td:nth-child(5)').html();

        if ($('#txt_modal_param').val() == 'menu_id') {
            // Loop each in data table
            $("#table_main tbody tr").each(function() {
                // Return data in row number = * (jquery mark * before popup (modal) )
                if ($(this).find('.order_no').html() == '*') {
                    // return selected product detail (code,name,units) to table row
                    $(this).find('.menu_id_1 > span').html(code);
                    $(this).find('.menu_name').html(name);
                    $(this).find('.price').html(note);   // default quantiy is '1'
                }
            });
            
            re_calculate_total_price();
        } else if ($('#txt_modal_param').val() == 'id_user') {
            $('#txt_IdUser').val(code);
            $('#txt_Username').val(name);
        } else if ($('#txt_modal_param').val() == 'menu_id') {
            $('#txt_OderNo').val(code);
            $('#txt_OrderDate').val(name);
            $('#txt_Customer').val(note);
            $('#txt_UserName').change();

            get_menu_detail(code);
        }

        $('#modal_form').modal('toggle');               // close modal
    });
    // /* search additional_items*/
    // $('.search_additional_items').click(function () {
    //     $.ajax({
    //         url:  '/additional_items/list',
    //         type:  'get',
    //         dataType:  'json',
    //         success: function  (data) {
    //             let rows =  '';
    //             var i = 1;
    //             data.additional_items.forEach(additional_items => {
    //                 rows += `
    //                 <tr class="d-flex">
    //                     <td class='col-1'>${i++}</td>
    //                     <td class='col-3'><a class='a_click' href='#'>${additional_items.type}</a></td>
    //                     <td class='col-5'></td>
    //                     <td class='col-3'></td>
    //                     <td class='hide'></td>
    //                 </tr>`;
    //             });
    //             $('#table_modal > tbody').html(rows);

    //             $('#model_header_1').text('Type');
    //             $('#model_header_2').text('Description');
    //             $('#model_header_3').text('Note');

    //         },
    //     });        
    //     // open popup
    //     $('#txt_modal_param').val('additional_items');
    //     $('#modal_form').modal();
    // });

    $('.search_id_user').click(function () {
        $.ajax({
            url:  '/customer/list',
            type:  'get',
            dataType:  'json',
            success: function  (data) {
                let rows =  '';
                var i = 1;
                data.customers.forEach(customer => {
                    rows += `
                    <tr class="d-flex">
                        <td class='col-1'>${i++}</td>
                        <td class='col-3'><a class='a_click' href='#'>${customer.id_user}</a></td>
                        <td class='col-5'>${customer.username}</td>
                        <td class='col-3'></td>
                        <td class='hide'></td>
                    </tr>`;
                });
                $('#table_modal > tbody').html(rows);

                $('#model_header_1').text('Customer ID');
                $('#model_header_2').text('Customer Name');
                $('#model_header_3').text('Note');

            },
        });        
        // open popup
        $('#txt_modal_param').val('id_user');
        $('#modal_form').modal();
    });

//--------------------------------------------------------------------------------------------------------------------
    $('.search_promotion_code').click(function () {
        $.ajax({
            url:  '/promotion/list',
            type:  'get',
            dataType:  'json',
            success: function  (data) {
                let rows =  '';
                var i = 1;
                data.promotions.forEach(promotion => {
                    rows += `
                    <tr class="d-flex">
                        <td class='col-1'>${i++}</td>
                        <td class='col-3'><a class='a_click' href='#'>${promotion.promotion_code}</a></td>
                        <td class='col-5'>${promotion.discount}</td>
                        <td class='col-3'></td>
                        <td class='hide'></td>
                    </tr>`;
                });
                $('#table_modal > tbody').html(rows);

                $('#model_header_1').text('Promotion');
                $('#model_header_2').text('Discount');
                $('#model_header_3').text('Note');

            },
        });        
        // open popup
        $('#txt_modal_param').val('promotion_code');
        $('#modal_form').modal();
    });

    $('.search_payment_method').click(function () {
        $.ajax({
            url:  '/paymentmethod/list',
            type:  'get',
            dataType:  'json',
            success: function  (data) {
                let rows =  '';
                var i = 1;
                data.payment_methods.forEach(payment_method => {
                    rows += `
                    <tr class="d-flex">
                        <td class='col-1'>${i++}</td>
                        <td class='col-3'><a class='a_click' href='#'>${payment_method.payment_method}</a></td>
                        <td class='col-5'>${payment_method.description}</td>
                        <td class='col-3'></td>
                        <td class='hide'></td>
                    </tr>`;
                });
                $('#table_modal > tbody').html(rows);

                $('#model_header_1').text('Payment Method');
                $('#model_header_2').text('Description');
                $('#model_header_3').text('Note');

            },
        });        
        // open popup
        $('#txt_modal_param').val('payment_method');
        $('#modal_form').modal();
    });

    $('.search_employee_id').click(function () {
        $.ajax({
            url:  '/employee/list',
            type:  'get',
            dataType:  'json',
            success: function  (data) {
                let rows =  '';
                var i = 1;
                data.employees.forEach(employee => {
                    rows += `
                    <tr class="d-flex">
                        <td class='col-1'>${i++}</td>
                        <td class='col-3'><a class='a_click' href='#'>${employee.employee_id}</a></td>
                        <td class='col-5'>${employee.name}</td>
                        <td class='col-3'></td>
                        <td class='hide'></td>
                    </tr>`;
                });
                $('#table_modal > tbody').html(rows);

                $('#model_header_1').text('Employee ID');
                $('#model_header_2').text('Employee Name');
                $('#model_header_3').text('Note');

            },
        });        
        // open popup
        $('#txt_modal_param').val('employee_id');
        $('#modal_form').modal();
    });

    $('table').on('focusin', 'td[contenteditable]', function() {
        $(this).data('val', $(this).html());
    }).on('input', 'td[contenteditable]', function() {
        //re_calculate_total_price();
    }).on('keypress', 'td[contenteditable]', function (e) {
        if (e.keyCode == 13) {
            return false;
        }
    }).on('focusout', 'td[contenteditable]', function() {
        var prev = $(this).data('val');
        var data = $(this).html();
        if (!numberRegex.test(data)) {
            $(this).text(prev);
        } else {
            $(this).data('val', $(this).html());
        }
        re_calculate_total_price();
    });

    // return from modal (popup)
    $('body').on('click', 'a.a_click', function() {
        //console.log($(this).parents('tr').html());
        //console.log($(this).parents('tr').find('td:nth-child(1)').html());
        var code = $(this).parents('tr').find('td:nth-child(2)').children().html();
        var name = $(this).parents('tr').find('td:nth-child(3)').html();
        var note = $(this).parents('tr').find('td:nth-child(4)').html();
        var pro = $(this).parents('tr').find('td:nth-child(5)').html();
        var pay = $(this).parents('tr').find('td:nth-child(6)').html();
        var em = $(this).parents('tr').find('td:nth-child(7)').html();

        if ($('#txt_modal_param').val() == 'menu_code') {
            $("#table_main tbody tr").each(function() {
                if ($(this).find('.order_no').html() == '*') {
                    $(this).find('.menu_code_1 > span').html(code);
                    //$(this).find('.product_name').html(name);
                    $(this).find('.total_price').html(name);
                    $(this).find('.amount').html("1");
                }
            });
            
            re_calculate_total_price();
        } else if ($('#txt_modal_param').val() == 'id_user') {
            $('#txt_IdUser').val(code);
            $('#txt_Username').val(name);
        } else if ($('#txt_modal_param').val() == 'payment_method') {
            $('#txt_PaymentMethod').val(code);
            $('#txt_Description').val(name);
        } else if ($('#txt_modal_param').val() == 'employee_id') {
            $('#txt_EmployeeID').val(code);
            $('#txt_EmployeeName').val(name);
        // } else if ($('#txt_modal_param').val() == 'menu_code') {
        //     $('#txt_MenuCode').val(code);
        //     $('#txt_EmployeeName').val(name);
        } else if ($('#txt_modal_param').val() == 'order_no') {
            $('#txt_OrderNo').val(code);
            $('#txt_OrderDate').val(name);
            $('#txt_IdUser').val(note);
            $('#txt_IdUser').change();
            $('#txt_PaymentMethod').val(pay);
            $('#txt_PaymentMethod').change();   
            
            get_order_detail(code);
        }

        $('#modal_form').modal('toggle');
    });

    // detect modal close form
    $('#modal_form').on('hidden.bs.modal', function () {
        re_order_no();
    });

    //disable_ui();
    reset_form();

    re_order_no();
    re_calculate_total_price();

    $('#btnNew').click(function () {
        reset_form();

        re_order_no();
        re_calculate_total_price();
    });
    $('#btnEdit').click(function () {
        $.ajax({
            url:  '/order/list',
            type:  'get',
            dataType:  'json',
            success: function  (data) {
                let rows =  '';
                var i = 1;
                data.orders.forEach(order => {
                    var order_date = order.date;
                    order_date = order_date.slice(0,10).split('-').reverse().join('/');
                    rows += `
                    <tr class="d-flex">
                        <td class='col-1'>${i++}</td>
                        <td class='col-3'><a class='a_click' href='#'>${order.order_no}</a></td>
                        <td class='col-5'>${order.date}</td>
                        <td class='col-3'>${order.id_user}</td>
                        <td class='hide'>${order.payment_method_id}</td>
                        <td class='hide'></td>
                    </tr>`;
                });
                $('#table_modal > tbody').html(rows);

                $('#model_header_1').text('Order No');
                $('#model_header_2').text('Order Date');
                $('#model_header_3').text('Customer ID');
                
                
                $('#txt_modal_param').val('order_no');
                $('#modal_form').modal(); 
            },
        });        
        // open popup
               
    });
    $('#btnSave').click(function () {

        var id_user = $('#txt_Username').val().trim();
        if (id_user == '') {
            alert('กรุณาระบุ Customer');
            $('#txt_IdUser').focus();
            return false;
        }
        var order_date = $('#txt_OrderDate').val().trim();
        if (!dateRegex.test(order_date)) {
            alert('กรุณาระบุวันที่ ให้ถูกต้อง');
            $('#txt_OrderDate').focus();
            return false;
        }
        if ($('#txt_OrderNo').val() == '<new>') {
            var token = $('[name=csrfmiddlewaretoken]').val();
                  
            $.ajax({
                url:  '/order/create',
                type:  'post',
                data: $('#form_order').serialize() + "&lineitem=" +lineitem_to_json(),
                headers: { "X-CSRFToken": token },
                dataType:  'json',
                success: function  (data) {
                    if (data.error) {
                        alert(data.error);
                    } else {
                        $('#txt_OrderNo').val(data.order.order_no)
                        alert('บันทึกสำเร็จ');
                    }                    
                },
            });  
        } else {
            var token = $('[name=csrfmiddlewaretoken]').val();
            console.log($('#form_order').serialize());
            console.log(lineitem_to_json());
            $.ajax({
                url:  '/order/update/' + $('#txt_OrderNo').val(),
                type:  'post',
                data: $('#form_order').serialize() + "&lineitem=" +lineitem_to_json(),
                headers: { "X-CSRFToken": token },
                dataType:  'json',
                success: function  (data) {
                    if (data.error) {
                        alert(data.error);
                    } else {
                        alert('บันทึกสำเร็จ');
                    }
                },
            }); 
        }
        
    });

    $('#btnDelete').click(function () {
        if ($('#txt_OrderNo').val() == '<new>') {
            alert ('ไม่สามารถลบ Order ใหม่ได้');
            return false;
        }
        if (confirm ("คุณต้องการลบ Order No : '" + $('#txt_OrderNo').val() + "' ")) {
            console.log('Delete ' + $('#txt_OrderNo').val());
            var token = $('[name=csrfmiddlewaretoken]').val();
            $.ajax({
                url:  '/order/delete/' + $('#txt_OrderNo').val(),
                type:  'post',
                headers: { "X-CSRFToken": token },
                dataType:  'json',
                success: function  (data) {
                    reset_form();
                },
            });            
        }
    });
    $('#btnPdf').click(function () {
        if ($('#txt_OrderNo').val() == '<new>') {
            alert ('กรุณาระบุ Order No');
            return false;
        }
        window.open('/order/pdf/' + $('#txt_OrderNo').val());
    });
    $('#btnPrint').click(function () {
        window.open('/order/report');
    });

});

function lineitem_to_json () {
    var rows = [];
    var i = 0;
    $("#table_main tbody tr").each(function(index) {
        if ($(this).find('.menu_code_1 > span').html() != '') {
            rows[i] = {};
            rows[i]["item_no"] = (i+1);
            rows[i]["menu_code"] = $(this).find('.menu_code_1 > span').html();
            rows[i]["unit_price"] = $(this).find('.unit_price').html();
            rows[i]["quantity"] = $(this).find('.quantity').html();
            rows[i]["product_total"] = $(this).find('.product_total').html();
            i++;
        }
    });
    var obj = {};
    obj.lineitem = rows;
    //console.log(JSON.stringify(obj));

    return JSON.stringify(obj);
}

function get_order_detail (order_no) {
    $.ajax({
        url:  'customer/detail/' + encodeURIComponent(order_no),
        type:  'get',
        dataType:  'json',
        success: function  (data) {
            //console.log(data.invoicelineitem.length);

            reset_table();
            for(var i=ROW_NUMBER;i<data.menu.length;i++) {
                $('.table-add').click();
            }
            var i = 0;
            $("#table_main tbody tr").each(function() {
                if (i < data.orderlineitem.length) {
                    $(this).find('.menu_code_1 > span').html(data.menu[i].menu_id);
                    $(this).find('.name').html(data.menu[i].menu_name);
                    $(this).find('.unit_price').html(data.menu[i].price);
                    $(this).find('.quantity').html(data.orderlineitem[i].quantity);
                }
                i++;
            });
            re_calculate_total_price();
        },
    });
}

function re_calculate_total_price () {
    var total_price = 0;
    $("#table_main tbody tr").each(function() {

        var menu_id = $(this).find('.menu_code_1 > span').html();
        //console.log (product_code);
        var unit_price = $(this).find('.unit_price').html();
        $(this).find('.unit_price').html(((unit_price)));
        var quantity = $(this).find('.quantity').html();
        $(this).find('.quantity').html(parseInt(quantity));
        if (menu_id != '') {
                var product_total = unit_price * quantity
            $(this).find('.product_total').html(formatNumber(product_total));
            total_price += product_total;
        }
    });
    var discount = $('#txt_Discount').val();
    $('#lbl_TotalPrice').text(formatNumber(total_price));
    $('#txt_TotalPrice').val($('#lbl_TotalPrice').text());
    $('#lbl_Discount').text(formatNumber(total_price*discount));
    $('#txt_Discount').val($('#lbl_Discount').text());
    $('#lbl_Remain').text(formatNumber(total_price*(1-discount)));
    $('#txt_Remain').val($('#lbl_Remain').text()); 
}


function reset_form() {
    $('#txt_OrderNo').attr("disabled", "disabled");
    $('#txt_OrderNo').val('<new>');

    reset_table();
    
    $('#txt_OrderDate').val(new Date().toJSON().slice(0,10).split('-').reverse().join('/'));

    $('#txt_IdUser').val('0000000000');
    $('#txt_Username').val('Unknown');
    $('#txt_PromotionCode').val('NoPromotion');
    $('#txt_Discount').val('0.00');
    $('#txt_PaymentMethod').val('');
    $('#txt_Description').val('');
    // $('#txt_EmployeeID').val('');
    // $('#txt_EmployeeName').val('');

    $('#lbl_TotalPrice').text('0.00');
    $('#lbl_Discount').text('0.00');
    $('#lbl_Remain').text('0.00');
}

function reset_table() {
    $('#table_main > tbody').html('');
    for(var i=1; i<= ROW_NUMBER; i++) {
        $('.table-add').click();
    }    
}

/* Add one row to table */
function add_last_one_row () {
    $('.table-add').click();                    // Call event click of button '+' in header of table, for add one row
}

function re_order_no () {
    var i = 1;
    $("#table_main tbody tr").each(function() {
        $(this).find('.order_no').html(i);
        i++;
    });
}


function disable_ui () {
    $('#txt_OrderDate').attr("disabled", "disabled");
    $('#btn_OrderDate').attr("disabled", "disabled");
}

function enable_ui () {
    $('#txt_OrderDate').removeAttr("disabled");
    $('#btn_OrderDate').removeAttr("disabled");
}



function formatNumber (num) {
    if (num === '') return '';
    num = parseFloat(num); 
    return num.toFixed(2).toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1,");
}

function isInt(n){
    return Number(n) === n && n % 1 === 0;
}

function isFloat(n){
    return Number(n) === n && n % 1 !== 0;
}

var dateRegex = /^(?=\d)(?:(?:31(?!.(?:0?[2469]|11))|(?:30|29)(?!.0?2)|29(?=.0?2.(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00)))(?:\x20|$))|(?:2[0-8]|1\d|0?[1-9]))([-.\/])(?:1[012]|0?[1-9])\1(?:1[6-9]|[2-9]\d)?\d\d(?:(?=\x20\d)\x20|$))?(((0?[1-9]|1[012])(:[0-5]\d){0,2}(\x20[AP]M))|([01]\d|2[0-3])(:[0-5]\d){1,2})?$/;
//var numberRegex = /^-?\d+\.?\d*$/;
var numberRegex = /^-?\d*\.?\d*$/


