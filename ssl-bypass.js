Java.perform(function () {

    console.log("[+] SSL Pinning Bypass Loaded");

    var TrustManagerImpl = Java.use(
        "com.android.org.conscrypt.TrustManagerImpl"
    );

    TrustManagerImpl.verifyChain.implementation = function (
        untrustedChain,
        trustAnchorChain,
        host,
        clientAuth,
        ocspData,
        tlsSctData
    ) {

        console.log("[+] Bypassing SSL Pinning: " + host);

        return untrustedChain;
    };
});