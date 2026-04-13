# DNS Configuration Guide for easypos.labinitial.com

## What Has Been Done Already:
✅ **Website Navigation Updated**: All HTML files (index.html, about.html, contact.html, etc.) now have a "Softwares" menu with "Labinitial POS" submenu that links to `https://easypos.labinitial.com`

## Steps to Configure Subdomain in Hostinger:

### Step 1: Log in to Hostinger
1. Go to [Hostinger](https://www.hostinger.com) and log into your account
2. Navigate to your **Hosting Dashboard**

### Step 2: Access DNS Management
1. In your Hosting Dashboard, find and click on **"DNS Zone Editor"** or **"DNS Management"**
2. Look for the section labeled **"DNS Records"** or **"Zone Editor"**

### Step 3: Add CNAME Record for Subdomain
You need to add a CNAME record that points `easypos.labinitial.com` to your Vercel app.

**Record Details to Add:**
```
Type: CNAME
Name/Host: easypos
Value/Points to: labinitialposretail.vercel.app
TTL: 300 (or Automatic)
Priority: (leave blank or set to 0)
```

**Alternative if the above doesn't work:**
```
Type: CNAME
Name/Host: easypos
Value/Points to: labinitialposretail-ggr7l0d31-arafats-projects-d0dd88ed.vercel.app
TTL: 300
```

### Step 4: Verify Current DNS Records
Based on your provided DNS information, you currently have:
- A record for `@` pointing to `216.198.79.1`
- CNAME record for `www` pointing to `3d268454691e06eb.vercel-dns-017.com`
- Various CAA records for SSL certificates

**DO NOT** modify or delete any existing records. Only **ADD** the new CNAME record for `easypos`.

### Step 5: Save Changes
1. Click **"Add Record"** or **"Save"**
2. Wait for DNS propagation (typically 5-30 minutes, but can take up to 24-48 hours)

## Step 6: Configure Vercel Project (Optional but Recommended)
1. Go to your Vercel dashboard: https://vercel.com
2. Select your **labinitialposretail** project
3. Go to **Settings** → **Domains**
4. Add the domain: `easypos.labinitial.com`
5. Vercel will verify the DNS configuration

## Step 7: Test the Configuration
After DNS propagation (wait at least 30 minutes):

1. **Test DNS resolution:**
   ```bash
   dig easypos.labinitial.com
   # or
   nslookup easypos.labinitial.com
   ```
   Should return: `labinitialposretail.vercel.app` or the Vercel edge network IP

2. **Test in browser:**
   - Visit `https://easypos.labinitial.com`
   - Should load your Labinitial POS app

3. **Test website navigation:**
   - Visit `https://labinitial.com`
   - Click on **Softwares** → **Labinitial POS**
   - Should redirect to `https://easypos.labinitial.com`

## Troubleshooting:

### If subdomain doesn't work after 24 hours:
1. **Clear DNS cache** on your computer
2. **Check DNS propagation** using: https://www.whatsmydns.net/#CNAME/easypos.labinitial.com
3. **Verify CNAME record** in Hostinger DNS Zone Editor
4. **Contact Hostinger support** if needed

### If you get SSL certificate errors:
1. Vercel automatically provisions SSL certificates via Let's Encrypt
2. Wait 1-2 hours after DNS propagation for SSL to be issued
3. Check Vercel project domains section for SSL status

## Important Notes:
- **DNS propagation time**: Changes can take time to propagate globally
- **Existing records**: Your current DNS setup for `labinitial.com` and `www.labinitial.com` will remain unchanged
- **Backup**: No changes to your website files are needed - navigation is already updated
- **Multiple environments**: The subdomain will point to your production Vercel deployment

## Support:
If you encounter any issues:
1. Check Hostinger DNS documentation
2. Contact Hostinger support for DNS-related issues
3. Contact Vercel support for domain verification issues

---
**Last Updated**: January 6, 2026  
**For**: Labinitial POS App Launch  
**Contact**: arafatinbusiness@gmail.com
