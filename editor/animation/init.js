requirejs(['ext_editor_io2', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {
        var io = new extIO({
            animation: function($expl, data){
                var checkioInput = data.in;
                if (!checkioInput){
                    return;
                }
                if (!data.ext || !data.ext.common) {
                    return;
                }
                var common = data.ext.common;
                var $first = $expl.find(".first");
                var $second = $expl.find(".second");

                var fillLetters = function($div, word) {
                    for (var i = 0; i < word.length; i++) {
                        var letter = word[i];
                        var $span = $("<span></span>").addClass(letter.toLowerCase());
                        $span.text(letter);
                        $div.append($span);
                    }
                };

                fillLetters($first, checkioInput[0]);
                fillLetters($second, checkioInput[1]);

                var paintLetter = function($where, letter) {
                    var $letter = $where.find("." + letter).eq(0);
                    $letter.removeClass();
                    $letter.addClass("highlight-letter");
                };

                var step = 200;
                for (var i = 0; i < common.length; i++) {
                    setTimeout(function() {
                        var l = common[i];
                        return function() {
                            paintLetter($first, l);
                            paintLetter($second, l);
                        };
                    }(), step * i);
                }

            },
            animationTemplateName: 'animation'

        });
        io.start();
    }
);
