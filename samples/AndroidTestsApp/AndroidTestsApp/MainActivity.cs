using System.Reflection;

using Android.App;
using Android.OS;
using Xamarin.Android.NUnitLite;
using CustomAndroidTestsConfiguration;

namespace AndroidTestsApp
{
  [Activity(Label = "AndroidTestsApp", MainLauncher = true)]
  public class MainActivity : ConfigurableTestActivity
  {
  }
}

