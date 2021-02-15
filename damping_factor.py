from pylab import *

def plot_damping_factor():
    k     = np.arange(0.,500.); #rad/m, wave number for ocean waves
    phi   = np.deg2rad(0);   #degrees angle between wind and radar wave direction
    u     = 5; #[m/s] wind speed 
    damping=calculate_damping_factor(0, u,phi, k);
    plot(k,10*np.log10(damping));
    ylim([0,15]);

def calculate_damping_factor(f,u,phi,k=None,cg=0.18, inc=deg2rad(20)):
    """calculate_damping_factor(f,u,phi)
    f=frequency [Hz] vector
    u=windspeed [m/s] scalar
    phi=degrees [rad] angle between wind and radar wave direction
    inc= degrees [rad] incidence angle
    """
######Parameters
    g     = 9.81; #m/s^2, gravity
    tau   = 7.3e-5; #m^3/s^2 ratio of surface tension and density
    eta   = 1.15e-3; #[Pa*s], dynamic viscosity
    rho   = 1038; #[kg/m^3], density of sea water
    E     = 0.0001; #[N/m], abs. value of dilatational modulus
    theta = np.deg2rad(220); #radians phase of dilatational modulus
    m     = 0.9; #unitless decrease in friction velocity (Gade et al. has it as 0.7)
    deltaN= 2.4; #unitless (nf-nc), difference between reduction in wave breaking due to oil
    u2uStar=0.035; #friction velocity on slick free ocean due to wind of u
#    cg    = 1;   #[m/s] group velocity of surface wave ???? I DONT KNOW THE RIGHT VALUE
    c     = 299792458; #[m/s] speed of light
#    phi   = np.deg2rad(0);   #degrees angle between wind and radar wave direction
#    u     = 5; #[m/s] wind speed

    if k is None:
      k = 4*np.pi*f/c *sin(inc); #from Eq 2 in Gade et al. bragg wave number is 2*k0 sin(theta)
    else:
      print("Not using frequency value. Wave numbers are provided.")
      #k     = np.arange(0.,500.); #rad/m, wave number for ocean waves

    w=np.sqrt(g*k+tau*k**3.); #angular freq of ocean waves ?[s/rad]?
    cp = w/k; #phase velocity of surface waves
    uStar=u*u2uStar;

    X= abs(E)*k**2/ np.sqrt(2*w**3*eta*rho);
    Y= abs(E)*k/(4*eta*w);
    y_numerator   = 1 + X*(cos(theta) - sin(theta)) + X*Y-Y*sin(theta)
    y_denominator = 1 + 2*X*(cos(theta) - sin(theta)) + 2*X**2
    y= y_numerator/y_denominator;

    deltaF = 1*k**2*eta*w/ (rho*(g+3*tau*k**2)); #viscous damping coefficient of CLEAN ocean surface
    deltaC = y*deltaF;

    muF = 0.04*cos(phi)*(uStar/cp)**2*w
    muC = 0.04*cos(phi)*(uStar*m/cp)**2*w#m*muF;

    term1 = (muC - 2*deltaC*cg) / (muF - 2*deltaF*cg)
    term2 = m**(deltaN-4.)*(2*uStar*np.sqrt(abs(cos(phi))*k/g))**deltaN;

    damping=term1*term2;
    return damping
