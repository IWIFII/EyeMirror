// pages/test/test.js

Page({

    /**
     * 页面的初始数据
     */
    data: { 
        content: "1",
    
        
    },
    
  

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        this.gettodolist(this)
    },

    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady: function () {

    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow: function () {
      this.gettodolist() 
    },

    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide: function () {

    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload: function () {

    },

    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh: function () {
        this.gettodolist()
        wx.stopPullDownRefresh({
          success: (res) => {},
        })
    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom: function () {

    },


    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function () {

    },

    jumptoTodoList: function(e) {
        wx.navigateTo({
 
            url: '/pages/todolist/todolist',
             
            })
      },
      jumptoChar: function(e) {
        wx.navigateTo({
 
            url: '/pages/char/char',
             
            })
      },
      
      gettodolist(e){
        var that = this;
        wx.request({
            url: 'http://192.168.31.11:8000/todolists/?format=json',
            header: {
              'Authorization': 'token 8eceebbff0c4b9e2d136f810a96a40a2d1f25f89'   
          },
          success: function(res) {
              var a =[]
              res.data.results.forEach(element => {
                a.push(element)
              });
              that.setData({
                content: a
                 
             }) 
            } 
      
          }) 
      }, 
      JsonToArray: function (data) {undefined
        let array = []; 
        for (let i in data) {undefined
        let data_obj = {};
        data_obj.code = i;
        data_obj.name = data[i];
        array.push(data_obj);
        }
        return array;
        }



})


