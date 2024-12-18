---
layout: base
title: "Limited Time Offer"
summary: "Limited Time Offer"
toplevel: Store
# toplevellink: /offer
---


<div id='product-component-1734376757015'></div>
<script type="text/javascript">
/*<![CDATA[*/
(function () {
  var scriptURL = 'https://sdks.shopifycdn.com/buy-button/latest/buy-button-storefront.min.js';
  if (window.ShopifyBuy) {
    if (window.ShopifyBuy.UI) {
      ShopifyBuyInit();
    } else {
      loadScript();
    }
  } else {
    loadScript();
  }
  function loadScript() {
    var script = document.createElement('script');
    script.async = true;
    script.src = scriptURL;
    (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(script);
    script.onload = ShopifyBuyInit;
  }
  function ShopifyBuyInit() {
    var client = ShopifyBuy.buildClient({
      domain: 'rdr0dk-ee.myshopify.com',
      storefrontAccessToken: 'a98222e68b67e5a4636fef2b3ff0dad8',
    });
    ShopifyBuy.UI.onReady(client).then(function (ui) {
      ui.createComponent('product', {
        id: '9724681060658',
        node: document.getElementById('product-component-1734376757015'),
        moneyFormat: '%24%7B%7Bamount%7D%7D',
        options: {
  "product": {
    "styles": {
      "product": {
        "@media (min-width: 601px)": {
          "max-width": "calc(25% - 20px)",
          "margin-left": "20px",
          "margin-bottom": "50px"
        }
      },
      "button": {
        ":hover": {
          "background-color": "#2e99c7"
        },
        "background-color": "#33aadd",
        ":focus": {
          "background-color": "#2e99c7"
        }
      }
    },
    "buttonDestination": "modal",
    "contents": {
      "options": false
    },
    "text": {
      "button": "View product"
    }
  },
  "productSet": {
    "styles": {
      "products": {
        "@media (min-width: 601px)": {
          "margin-left": "-20px"
        }
      }
    }
  },
  "modalProduct": {
    "contents": {
      "img": false,
      "imgWithCarousel": true,
      "button": false,
      "buttonWithQuantity": true
    },
    "styles": {
      "product": {
        "@media (min-width: 601px)": {
          "max-width": "100%",
          "margin-left": "0px",
          "margin-bottom": "0px"
        }
      },
      "button": {
        ":hover": {
          "background-color": "#2e99c7"
        },
        "background-color": "#33aadd",
        ":focus": {
          "background-color": "#2e99c7"
        }
      }
    },
    "text": {
      "button": "Add to cart"
    }
  },
  "option": {},
  "cart": {
    "styles": {
      "button": {
        ":hover": {
          "background-color": "#2e99c7"
        },
        "background-color": "#33aadd",
        ":focus": {
          "background-color": "#2e99c7"
        }
      }
    },
    "text": {
      "total": "Subtotal",
      "button": "Checkout"
    }
  },
  "toggle": {
    "styles": {
      "toggle": {
        "background-color": "#33aadd",
        ":hover": {
          "background-color": "#2e99c7"
        },
        ":focus": {
          "background-color": "#2e99c7"
        }
      }
    }
  }
},
      });
    });
  }
})();
/*]]>*/
</script>

</div> <!-- end ofbuy button code -->

<br/><br/><br/>

When these 500 copies run out, you can still <a href="/publications/">buy copies</a> for the regular price.
