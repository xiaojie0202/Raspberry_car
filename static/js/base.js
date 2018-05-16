var viewHeight = document.documentElement.clientHeight; //获取页面的宽度


// 隐藏浏览器连接
window.onload = function () {
    if (document.documentElement.scrollHeight <= document.documentElement.clientHeight) {
        bodyTag = document.getElementsByTagName('body')[0];
        bodyTag.style.height = document.documentElement.clientWidth / screen.width * screen.height + 'px';
    }
    setTimeout(function () {
        window.scrollTo(0, 1)
    }, 0);
};

// 检测横竖屏
function orient() {
    if (window.orientation == 0 || window.orientation == 180) {
        $("#lesesss").show();  //当竖屏的时候为body增加一个class
        return false
    }
    else if (window.orientation == 90 || window.orientation == -90) {
        $("#lesesss").hide(); //当横屏的时候为body移除这个class
        return true
    }
}

// 监听手机翻转事件
$(window).bind('orientationchange', function (e) {
    orient(); //旋转屏幕端口socket
    var viewHeight = document.documentElement.clientHeight;
    $('body').height(viewHeight);
    $('.main').height(viewHeight);
    $('.portrait').height(viewHeight);
    location.reload();
});


// 读完文档
$(function () {
    orient();
    $('body').height(viewHeight);
    $('.main').height(viewHeight);
    $('.portrait').height(viewHeight);
    window.ontouchstart = function (e) {
        e.preventDefault();
    };
});