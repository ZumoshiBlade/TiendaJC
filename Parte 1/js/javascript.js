$(document).ready(function(){
    $('.category-list .category-item[category="all"]').addClass('ct_item-active');

    $('.category-item').click(function(){

        var catProduct = $(this).attr('category');

        $('.category-item').removeClass('ct_item-active');
        $(this).addClass('ct_item-active');

        $('.product-item').hide();

        $('.product-item[category="'+catProduct+'"]').show();
    });

    $('.category-item[category="all"]').click(function(){
        $('.product-item').show();
    });
});
