
/* 
 * This is a bar chart of regional responses by category, shown on top of 
 * a bar chart of national responses by category
 * argument: regional_poll_responses 
 *           - list of responses by category for a region (what unit?)
 * arguments: national_poll_responses 
 *           - list of responses by category total (what unit?)
 */

window.onload=function() {
    var canvasWidth = 390;
    var factor = (canvasWidth/107);

    var paper = Raphael(document.getElementById("chart"), canvasWidth, 120);
	var x = 0;
    var y = 5;
    var darkHeight = 10;
    var lightHeight = 30;
    var fillerWidth = 2; 
	for (var i=0; i < regional_poll_responses.length; i++) {
        var width = regional_poll_responses[i]['percentage']*factor ;
        var lightRectangle = paper.rect(x,y,width,lightHeight);
		lightRectangle.attr({
			fill: regional_poll_responses[i]['color'],
			stroke: regional_poll_responses[i]['color'],
			opacity: 0.30
		});
///////////test 
		var lang = document.getElementById("B1"); 
		var	percentageNo = TransNum(regional_poll_responses[i]['percentage']) 
        var percentageText = paper.text(x+width/2.0,y+lightHeight/2.0,percentageNo);
         percentageText.attr({
            fill: regional_poll_responses[i]['color'],
            stroke: regional_poll_responses[i]['color'],
            font: "13px 'Arial'",
            opacity: 1
        });

        var darkRectangle = paper.rect(x,y+lightHeight,width,darkHeight);
		darkRectangle.attr({
			fill: regional_poll_responses[i]['color'],
			stroke: regional_poll_responses[i]['color'],
			opacity: 1
		});
        x = x + width;
        
        var filler = paper.rect(x,y,fillerWidth,darkHeight + lightHeight);
        filler.attr({
            fill: "white",
            stroke: "white"
        });

        x = x + fillerWidth;
	};
    y = y+lightHeight;
    x=0;
    
    for (var i=0; i < national_poll_responses.length; i++) {
        var width = national_poll_responses[i]['percentage']*factor;
        var r = paper.rect(x, y+30, width, 5);
        r.attr({
            fill: national_poll_responses[i]['color'],
            stroke: national_poll_responses[i]['color'],
            opacity: 0.70
        });
        x = x + width;
        var filler = paper.rect(x,y+30,fillerWidth,5);
        filler.attr({
            fill: "white",
            stroke: "white"
        });

        x = x + fillerWidth;
    }
};

function TransNum(number)
	{
		var lang = document.getElementById("B1");
		if (lang != undefined)
			{
				if (lang.title == "Boys")
					{
						return number + "%";
					}
				else
					{
						var conv = new String(number);
						conv = conv.replace('.',',');
						conv = conv.replace('0','٠').replace('0','٠').replace('0','٠');
						conv = conv.replace('1','١').replace('1','١').replace('1','١');
						conv = conv.replace('2','٢').replace('2','٢').replace('2','٢');
						conv = conv.replace('3','٣').replace('3','٣').replace('3','٣');
						conv = conv.replace('4','٤').replace('4','٤').replace('4','٤');
						conv = conv.replace('5','٥').replace('5','٥').replace('5','٥');
						conv = conv.replace('6','٦').replace('6','٦').replace('6','٦');
						conv = conv.replace('7','٧').replace('7','٧').replace('7','٧');
						conv = conv.replace('8','٨').replace('8','٨').replace('8','٨');
						conv = conv.replace('9','٩').replace('9','٩').replace('9','٩');
						return "%" + conv;
					}
			}
		else
		{
			return number + "%";
		}
	};