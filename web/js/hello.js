$(document).ready(function(){

 // G2 对数据源格式的要求，仅仅是 JSON 数组，数组的每个元素是一个标准 JSON 对象。
// Step 1: 创建 Chart 对象
    const chart = new G2.Chart({
        container: 'c1', // 指定图表容器 ID
        width : 800, // 指定图表宽度
        height : 400 // 指定图表高度
    });
// Step 2: 载入数据源
    chart.source(dataInfo);
// Step 3：创建图形语法，绘制柱状图，由 genre 和 sold 两个属性决定图形位置，genre 映射至 x 轴，sold 映射至 y 轴
    chart.interval().position('genre*sold').color('genre')
// Step 4: 渲染图表
    chart.render();

    // Step 1: 创建 Chart 对象
    const chart1 = new G2.Chart({
        container: 'c2', // 指定图表容器 ID
        width : 800, // 指定图表宽度
        height : 400 // 指定图表高度
    });
// Step 2: 载入数据源
    chart1.source(dataInfo1);
// Step 3：创建图形语法，绘制柱状图，由 genre 和 sold 两个属性决定图形位置，genre 映射至 x 轴，sold 映射至 y 轴
    chart1.interval().position('genre*sold').color('genre')
// Step 4: 渲染图表
    chart1.render();

    // Step 1: 创建 Chart 对象
    const chart2 = new G2.Chart({
        container: 'c3', // 指定图表容器 ID
        width : 800, // 指定图表宽度
        height : 400 // 指定图表高度
    });
// Step 2: 载入数据源
    chart2.source(dataInfo2);
// Step 3：创建图形语法，绘制柱状图，由 genre 和 sold 两个属性决定图形位置，genre 映射至 x 轴，sold 映射至 y 轴
    chart2.interval().position('genre*sold').color('genre')
// Step 4: 渲染图表
    chart2.render();

    // Step 1: 创建 Chart 对象
    const chart3 = new G2.Chart({
        container: 'c4', // 指定图表容器 ID
        width : 800, // 指定图表宽度
        height : 400 // 指定图表高度
    });
// Step 2: 载入数据源
    chart3.source(dataInfo3);
// Step 3：创建图形语法，绘制柱状图，由 genre 和 sold 两个属性决定图形位置，genre 映射至 x 轴，sold 映射至 y 轴
    chart3.interval().position('genre*sold').color('genre')
// Step 4: 渲染图表
    chart3.render();

// Step 1: 创建 Chart 对象
    const chart4 = new G2.Chart({
        container: 'c5', // 指定图表容器 ID
        width : 800, // 指定图表宽度
        height : 400 // 指定图表高度
    });
// Step 2: 载入数据源
    chart4.source(dataInfo4);
// Step 3：创建图形语法，绘制柱状图，由 genre 和 sold 两个属性决定图形位置，genre 映射至 x 轴，sold 映射至 y 轴
    chart4.interval().position('genre*sold').color('genre')
// Step 4: 渲染图表
    chart4.render();

    // Step 1: 创建 Chart 对象
    const chart5 = new G2.Chart({
        container: 'c6', // 指定图表容器 ID
        width : 800, // 指定图表宽度
        height : 400 // 指定图表高度
    });
// Step 2: 载入数据源
    chart5.source(dataInfo5);
// Step 3：创建图形语法，绘制柱状图，由 genre 和 sold 两个属性决定图形位置，genre 映射至 x 轴，sold 映射至 y 轴
    chart5.interval().position('genre*sold').color('genre')
// Step 4: 渲染图表
    chart5.render();
});