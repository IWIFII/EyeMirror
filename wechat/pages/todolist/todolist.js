// // pages/todolist/todolist.js
// Page({

//     /**
//      * 页面的初始数据
//      */
//     data: {

//     },

//     /**
//      * 生命周期函数--监听页面加载
//      */
//     onLoad: function (options) {

//     },

//     /**
//      * 生命周期函数--监听页面初次渲染完成
//      */
//     onReady: function () {

//     },

//     /**
//      * 生命周期函数--监听页面显示
//      */
//     onShow: function () {

//     },

//     /**
//      * 生命周期函数--监听页面隐藏
//      */
//     onHide: function () {

//     },

//     /**
//      * 生命周期函数--监听页面卸载
//      */
//     onUnload: function () {

//     },

//     /**
//      * 页面相关事件处理函数--监听用户下拉动作
//      */
//     onPullDownRefresh: function () {

//     },

//     /**
//      * 页面上拉触底事件的处理函数
//      */
//     onReachBottom: function () {

//     },

//     /**
//      * 用户点击右上角分享
//      */
//     onShareAppMessage: function () {

//     }
// })

Page({
    /**
     * 页面的初始数据
     */
    data: {
        list: [

        ],
        evtContent: '',
        hiddenmodalput: true,
        // scrollHeight: '1000rpx', // scroll-view高度
        startX: 0, // 开始X坐标
        startY: 0, // 开始Y坐标

    },

    // 手指触摸动作开始
    touchStart: function (e) {
        let that = this;
        //开始触摸时 重置所有删除
        that.data.list.forEach(function (v, i) {
            if (v.isTouchMove) v.isTouchMove = false; // 只操作为true的
        })
        // 记录手指触摸开始坐标
        that.setData({
            startX: e.changedTouches[0].clientX, // 开始X坐标
            startY: e.changedTouches[0].clientY, // 开始Y坐标
            list: that.data.list
        })
    },

    // 手指触摸后移动
    touchMove: function (e) {
        let that = this,
            index = e.currentTarget.dataset.index, // 当前下标
            startX = that.data.startX, // 开始X坐标
            startY = that.data.startY, // 开始Y坐标
            touchMoveX = e.changedTouches[0].clientX, // 滑动变化坐标
            touchMoveY = e.changedTouches[0].clientY, // 滑动变化坐标
            // 获取滑动角度
            angle = that.angle({
                X: startX,
                Y: startY
            }, {
                X: touchMoveX,
                Y: touchMoveY
            });
        // 判断滑动角度
        that.data.list.forEach(function (v, i) {
            v.isTouchMove = false
            // 滑动超过30度角 return
            if (Math.abs(angle) > 30) return;
            if (i == index) {
                // 右滑
                if (touchMoveX > startX)
                    v.isTouchMove = false
                // 左滑
                else
                    v.isTouchMove = true
            }
        })
        // 更新数据
        that.setData({
            list: that.data.list
        })
    },

    // 计算滑动角度
    angle: function (start, end) {
        let that = this,
            _X = end.X - start.X,
            _Y = end.Y - start.Y;
        // 返回角度 /Math.atan()返回数字的反正切值
        return 360 * Math.atan(_Y / _X) / (2 * Math.PI);
    },

    // 删除
    delList: function (e) {
        let that = this,
            index = e.currentTarget.dataset.index; // 当前下标
        // 切割当前下标元素，更新数据 
        wx.request({
            url: 'http://192.168.31.11:8000/todolists/' + that.data.list[index].id,
            header: {
                'Authorization': 'token 8eceebbff0c4b9e2d136f810a96a40a2d1f25f89'
            },
            method: "DELETE",
            success: function (res) {
                console.log(res)
                if (res.data == "") {
                    that.data.list.splice(index, 1);

                    that.setData({
                        list: that.data.list
                    })
                } else {
                    wx.showToast({
                        title: '删除失败', // 标题
                        icon: 'error', // 图标类型，默认success
                        duration: 1500 // 提示窗停留时间，默认1500ms

                    })
                }


            },
            fail: function () {
                wx.showToast({
                    title: '操作失败', // 标题
                    icon: 'error', // 图标类型，默认success
                    duration: 1500 // 提示窗停留时间，默认1500ms

                })
            }

        })

    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        let that = this;

        that.gettodolist(this)
        // 动态获取屏幕高度
        // that.setData({
        //     scrollHeight: wx.getSystemInfoSync().screenHeight
        // })
    },

    gettodolist(e) {
        var that = this;
        wx.request({
            url: 'http://192.168.31.11:8000/todolists/?format=json',
            header: {
                'Authorization': 'token 8eceebbff0c4b9e2d136f810a96a40a2d1f25f89'
            },
            success: function (res) {
                var a = []
                res.data.results.forEach(element => {
                    a.push(element)
                });
                that.setData({
                    list: a

                })
                console.log(that.data.list)
            }

        })
    },

    modalinput: function () {
        this.setData({
            hiddenmodalput: !this.data.hiddenmodalput
        })
    },

    confirm: function(e) {
        var that = this
        if(this.data.evtContent.length>0 && this.data.evtContent.length<30){
            wx.request({
                url: 'http://192.168.31.11:8000/todolists/',
                header: {
                  'Authorization': 'token 8eceebbff0c4b9e2d136f810a96a40a2d1f25f89'
              },
              data:{
                  content: this.data.evtContent
              },
              method:'post',
              success: function (res) {
                  that.gettodolist() 
              }
              }
              )

            
            
        }else{
            wx.showToast({
                title: '内容过长', // 标题
                icon: 'error', // 图标类型，默认success
                duration: 1500 // 提示窗停留时间，默认1500ms
            })
        }
        this.setData({
            evtContent : ''
         });
         this.modalinput()

    },

      //事件
  textBlur: function(e){
    if(e.detail&&e.detail.value.length>0){
      if(e.detail.value.length>30){
      }else{
         this.setData({
            evtContent : e.detail.value
         });
      }
    }else{
       this.setData({
          evtContent : ''
       });
       evtData.evaContent = '';
    }
    this.confirm()
 },
})