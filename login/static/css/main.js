getAssetLocation = function(){
	var assetUrl = document.URL;
	var domainParam = assetUrl.replace(/^([^\?]*)\?(.*)(\&*)domain=([^&]+)(.*)$/ig,'$4');
	var assetLoc = "//cdn.ucl.ac.uk/";
	if(typeof domainParam!=='undefined'){

		switch(domainParam){
			case "static":
				assetLoc = "//static.ucl.ac.uk/";
			break;
			case "local":
				assetLoc = "//static-local/";
			break;
			case "uat":
				assetLoc = "//static-uat.ucl.ac.uk/";
			break;
		}
	}
	return assetLoc;
}
var assetLocation = getAssetLocation();
var urlArgs = "";

if(typeof globalSiteSpecificVars.mainJsVersion !=='undefined'){
	urlArgs = "v" + globalSiteSpecificVars.mainJsVersion;
}

require.config({
	baseUrl: assetLocation + 'indigo/js/lib',
	urlArgs : urlArgs,
	config: {
        text: {
            useXhr: function (url, protocol, hostname, port) {
                // allow cross-domain requests
                // remote server allows CORS
                return true;
            }
        }
    },
	paths: {
		app: '../app',
		theme: '../../../skins/indigo-theme-js/app',
        templates: '../../../skins/indigo-theme-js/templates',
		
        allsite: 'all-site.min',
		//libaries
		jquery: globalSiteSpecificVars.pathToJquery,
		//jquery: 'jquery-1.9.1.min',
		modernizr: 'modernizr-custom',
        underscore: [
                        '//cdnjs.cloudflare.com/ajax/libs/underscore.js/1.6.0/underscore-min'
                        ,'underscore-1.6.0.min'
        ],
        backbone: [
                    '//cdnjs.cloudflare.com/ajax/libs/backbone.js/1.1.2/backbone-min'
                    ,'backbone-1.1.2.min'
        ],
		fastclick: 'fastclick',
		jqueryUi: assetLocation + 'skins/indigo-theme-js/lib/jquery-ui-1.8.18.custom.min',
		jqueryTmpl: assetLocation + 'skins/indigo-theme-js/lib/jquery.tmpl.min',
		jwplayer: 'jwplayer',
		googleAnalyticsLib: 'googleAnalytics.min',
		handleBars: 'handlebars.min',
		typeAheadBundle: 'typeahead.bundle.min',
		owl: 'owl.carousel.min',

		// Theme specific
		searchPack: assetLocation + 'skins/indigo-theme-js/lib/search-pack.min',
		smoothScroll: assetLocation + 'skins/indigo-theme-js/lib/smoothscroll.min',
		scrollSpy: assetLocation + 'skins/indigo-theme-js/lib/scrollspy.min',
		iframeresizer: assetLocation + 'skins/indigo-theme-js/lib/iframeheight.min',
		researchImpactCaseStudyFeed: 'researchImpactCaseStudyFeed.min',
		rps: 'rps.min'

		//hashchange: assetLocation + 'skins/indigo-theme-js/lib/jquery.hashchange.min',
	},
	shim: {
		allsite: {
			deps: ['jquery'],
			exports: 'gen'
		},
		underscore: {
			exports: '_'
		},
		backbone: {
			deps: ['underscore', 'jquery'],
			exports: 'B'
		},
		modernizr: {
			exports: 'Modernizr'
		},
		jqueryUi: {
			deps: ['jquery']
		},
		jwplayer: {
			exports: 'jwplayer'
		},
		jqueryTmpl: {
			deps: ['jquery']
		},
		googleAnalyticsLib: {
			exports: 'ga'
		},
		typeAheadBundle: {
			deps: ['jquery']
			,exports: 'Bloodhound'
		},
		handleBars : {
			exports: 'Handlebars'
		},
		scrollSpy: {
			deps: ['jquery']
		},
		researchImpactCaseStudyFeed: {
			deps: ['underscore', 'jquery', 'B']
		},
		rps: {
			deps: ['jquery']
		},
		owl: {
			deps: ['jquery']
		},
		searchPack: {
			deps: ['jquery']
		},
		palette: {
			deps: ['jquery']
		},
		iframeresizer: {
			deps: ['jquery']

		}
	}
});
