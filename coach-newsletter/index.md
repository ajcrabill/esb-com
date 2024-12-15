---
layout: base
title: "Newsletter"
summary: "The Effective School Board Coach Newsletter Landing Page"
toplevel: "The Effeective School Board Coach"
# toplevellink: /Newsletter
---


<style type="text/css">

.pricing-section {
  padding: 50px 0;
}

.pricing-container {
  display: flex;
  max-width: 1200px;
  margin: 0 auto;
  gap: 20px;
  flex-wrap: wrap;
  justify-content: center;
}

.plan {
  background: #fff;
  border-radius: 8px;
  padding: 30px;
  flex: 1 1 250px;
  box-shadow: 0 0 10px rgba(0,0,0,0.05);
  max-width: 280px;
  position: relative;
}

.plan.most-popular {
  background: linear-gradient(to bottom, #ffe3ee, #ffeaf3);
  border: 2px solid #f2c0d2;
}

.plan.most-popular .badge {
  position: absolute;
  top: 20px;
  right: 20px;
  background: #000;
  color: #fff;
  font-size: 0.75rem;
  text-transform: uppercase;
  padding: 5px 8px;
  border-radius: 4px;
}

.plan-title {
  font-size: 1.5rem;
  margin: 0 0 10px;
  font-weight: bold;
}

.plan-subtitle {
  font-size: 0.9rem;
  color: #555;
  margin-bottom: 20px;
  line-height: 1.4;
}

.price-container {
  display: flex;
  align-items: baseline;
  margin-bottom: 5px;
}

.price {
  font-size: 2.5rem;
  font-weight: bold;
}

.price-term {
  margin-left: 5px;
  font-size: 1rem;
  color: #555;
}

.billed-annually {
  font-size: 0.9rem;
  margin: 0 0 20px;
  color: #555;
}

.billed-annually .original-price {
  text-decoration: line-through;
  color: #999;
  font-size: 0.8rem;
  margin-left: 5px;
}

.cta-button {
  display: inline-block;
  background: #000;
  color: #fff;
  padding: 10px 20px;
  margin-bottom: 20px;
  text-decoration: none;
  border-radius: 4px;
  font-weight: bold;
  text-align: center;
}

.features {
  list-style: none;
  padding: 0;
  margin: 0 0 15px;
}

.features li {
  margin-bottom: 10px;
  padding-left: 20px;
  position: relative;
  font-size: 0.95rem;
}

.features li::before {
  content: '✓';
  position: absolute;
  left: 0;
  color: #ff5da0;
  font-weight: bold;
}

.note {
  font-size: 0.8rem;
  color: #777;
  line-height: 1.4;
}

/* Responsive adjustments */
@media (max-width: 992px) {
  .plan {
    max-width: 300px;
    flex: 1 1 300px;
  }
}

@media (max-width: 768px) {
  .pricing-container {
    flex-direction: column;
    align-items: center;
  }
  .plan {
    max-width: 80%;
  }
}

</style>

<section class="pricing-section">
  <div class="pricing-container">

    <!-- Free Plan -->
  <div class="plan">
      <h3 class="plan-title">Free</h3>
      <p class="plan-subtitle">Get the foundations right to set up your business.</p>
      <div class="price-container">
        <span class="price">$55</span><span class="price-term">/mo*</span>
      </div>
      <p class="billed-annually">Billed annually <span class="original-price">$69/mo</span></p>
      <a href="#" class="cta-button">Get Started →</a>
      <ul class="features">
        <li>0% Transaction Fee</li>
        <li>50 Landing Pages</li>
        <li>1,250 Marketing Emails</li>
        <li>1 Product</li>
        <li>250 Contacts</li>
        <li>1 Website</li>
      </ul>
      <p class="note">*+ applicable taxes. Only available to new users.</p>
    </div>

    <!-- Basic Plan -->
  <div class="plan">
      <h3 class="plan-title">Basic</h3>
      <p class="plan-subtitle">Everything you need to start your business.</p>
      <div class="price-container">
        <span class="price">$119</span><span class="price-term">/mo*</span>
      </div>
      <p class="billed-annually">Billed annually <span class="original-price">$149/mo</span></p>
      <a href="#" class="cta-button">Get Started →</a>
      <ul class="features">
        <li>0% Transaction Fee</li>
        <li>Unlimited Landing Pages</li>
        <li>Unlimited Marketing Emails</li>
        <li>3 Products</li>
        <li>10,000 Contacts</li>
        <li>1 Website</li>
      </ul>
      <p class="note">*+ applicable taxes</p>
    </div>

    <!-- Premium Plan -->
  <div class="plan most-popular">
      <div class="badge">Most Popular</div>
      <h3 class="plan-title">Premium</h3>
      <p class="plan-subtitle">Expand your business and get serious about growing.</p>
      <div class="price-container">
        <span class="price">$159</span><span class="price-term">/mo*</span>
      </div>
      <p class="billed-annually">Billed annually <span class="original-price">$199/mo</span></p>
      <a href="#" class="cta-button">Get Started →</a>
      <ul class="features">
        <li>0% Transaction Fee</li>
        <li>Unlimited Landing Pages</li>
        <li>Unlimited Marketing Emails</li>
        <li>15 Products</li>
        <li>25,000 Contacts</li>
        <li>1 Website</li>
      </ul>
      <p class="note">*+ applicable taxes</p>
    </div>

    <!-- Masterclass Plan -->
  <div class="plan">
      <h3 class="plan-title">Masterclass</h3>
      <p class="plan-subtitle">Scale your business with advanced features.</p>
      <div class="price-container">
        <span class="price">$319</span><span class="price-term">/mo*</span>
      </div>
      <p class="billed-annually">Billed annually <span class="original-price">$399/mo</span></p>
      <a href="#" class="cta-button">Get Started →</a>
      <ul class="features">
        <li>0% Transaction Fee</li>
        <li>Unlimited Landing Pages</li>
        <li>Unlimited Marketing Emails</li>
        <li>100 Products</li>
        <li>100,000 Contacts</li>
        <li>3 Websites</li>
      </ul>
      <p class="note">*+ applicable taxes</p>
    </div>

  </div>
</section>
