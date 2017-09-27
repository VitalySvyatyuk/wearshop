var link = '/api/v/1/products/'

var loadData = function() {
  $.ajax({
    type: 'GET',
    url: link,
    success: function(data) {
      link = data.next;
      var items = [];
      $.each(data.results, function(key, value) {
        items.push(
            '<div class="col-xs-6 col-sm-4 col-md-3">'
          + '<div class="product">'
          + '<img class="shoe-img" src='+value.img+'>'
          + '<div class="data">'
          + '<div class="padding-left name">'
          + '<p class="mizonu">'+value.name+'</p>'
          + '<p class="soccer">'+value.category+'</p></div>'
          + '<div class="padding-left price-div">'
          + '<p class="price">$'+value.price+'</p>'
          + '</div></div></div></div>'
        );
      });
      $('#div-goods').append(items.join(""));
      if (link === null) {
        $('#show-more').hide()
      };
    }
  })
};

$(loadData);

$(document).on('click','#show-more',function(){
  loadData();
})