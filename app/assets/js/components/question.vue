<template>

<div>
    <div class="wrapper">
    <div class="l-container">
        <h2 class="title">投票画面</h2>
        <div class="grid">
        <div class="grid__inner">
            <div class="grid__item">
            <div class="js-post count" data-initial="hatsushi">
                <p class="count__name js-name-hatsushi">はつし</p>
                <p class="count__num js-count js-count-hatsushi">0</p>
            </div>
            </div>
            <div class="grid__item">
            <div class="js-post count" data-initial="masakuni">
                <p class="count__name js-name-masakuni">まさくに</p>
                <p class="count__num js-count js-count-masakuni">0</p>
            </div>
            </div>
            <div class="grid__item">
            <div class="js-post count" data-initial="tk">
                <p class="count__name js-name-tk">TK</p>
                <p class="count__num js-count js-count-tk">0</p>
            </div>
            </div>
            <div class="grid__item">
            <div class="js-post count" data-initial="kaz">
                <p class="count__name js-name-kaz">Kaz</p>
                <p class="count__num js-count js-count-kaz">0</p>
            </div>
            </div>
        </div>
        </div>
    </div>
    </div>

    <!-- <div class="layer js-layer dn">
        <img class="layer__loading js-layer-loading dn" src="https://lig824.github.io/event/public/assets/images/loading.gif" alt="">
    </div> -->
    <!-- <div> -->
    <!-- <script src="https://www.gstatic.com/firebasejs/4.6.0/firebase.js"></script> -->
    <!-- </div> -->
</div>
</template>

<script>
export default {
    name: 'question',
    props:['question'],
    mounted() {
        console.log('mounted()');
        console.log(this.question);
    }
}
</script>

<style>

* {
    box-sizing: border-box
}

.l-container {
    padding-left: 30px;
    padding-right: 30px;
}

.wrapper {
    padding: 20px 0;
}

.title {
  margin-top: 0;
    text-align: center;
    color: #2196f3;
    font-size: 25px;
    line-height: 1.4;
    text-overflow: ellipsis;
}

.grid {
    .grid__inner {
        display: flex;
        flex-wrap: wrap;
        margin: -13px;
    }
    .grid__item {
        width: 50%;
        padding: 13px;
    }
}

.count {
    position: relative;
    padding: 15px 0;
    cursor: pointer;
    border: 1px solid #d0cfcf;
    border-radius: 6px;
    background-color: #fff;
    -webkit-tap-highlight-color:rgba(0,0,0,0);
    &.count--screen {
        cursor: default;
    }
}

.count__name {
    display: block;
    position: relative;
    margin-top: 10px;
    margin-bottom: 0;
    line-height: 1;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
}

.count__num {
    margin-top: 10px;
    margin-bottom: 0;
    line-height: 1;
    color: #2196f5;
    text-align: center;
    font-size: 45px;
    font-weight: bold;
}
</style>