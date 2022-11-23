$("#table-selection").change(function () {
    const url = '/ajax/load-data-entry-form/';  
    const tbOption = $(this).val();
    $.ajax({                      
      url: url,                    
      data: {
        'tb_option': tbOption       
      },
      success: function (data) {
        const arr = data.split('<break/>');
        const schema = '<h5 class="card-title mb-4">Table Schema</h5>' + arr[0];
        const form = arr[1];
        $("#insert-data-entry-form").html(form);  
        $("#table-schema").html(schema);
      }
    });
});