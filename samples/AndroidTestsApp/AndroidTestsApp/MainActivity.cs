using System.Reflection;

using Android.App;
using Android.OS;
using Xamarin.Android.NUnitLite;
using CustomAndroidTestsConfiguration;

namespace AndroidTestsApp
{
  [Activity(Name = "com.sample.tests.app.MainActivity", Label = "AndroidTestsApp", MainLauncher = true)]
  public class MainActivity : ConfigurableTestActivity
  {
  }
}

