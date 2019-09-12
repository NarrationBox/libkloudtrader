'''archive'''


'''
def hilbert_transform_inst_trendline(data):
    """Hilbert Transform - Instantaneous Trendline"""
    try:
        logger.info(
            'Calculating Hilbert Transform - Instantaneous Trendline...')
        htit_data = talib.HT_TRENDLINE(data)
        return htit_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def hilbert_transform_dom_cyc_per(data):
    """Hilbert Transform - Dominant Cycle Period"""
    try:
        logger.info('Calculating Hilbert Transform - Dominant Cycle Period')
        htdcp_data = talib.HT_DCPERIOD(data)
        return htdcp_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def hilbert_transform_dom_cyc_phase(data):
    """Hilbert Transform - Dominant Cycle Phase"""
    try:
        logger.info('Calculating Hilbert Transform - Dominant Cycle Phase')
        htdcp_data = talib.HT_DCPHASE(data)
        return htdcp_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def hilbert_transform_phasor_components(close):
    """Hilbert Transform - Phasor Components"""
    try:
        logger.info("Calculating Hilbert Transform - Phasor Components...")
        inphase_data, quadrature_data = talib.HT_PHASOR(close)
        df = pd.DataFrame()
        df['inphase'] = inphase_data
        df['quadrature'] = quadrature_data
        return df
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def hilbert_transform_sine_wave(data):
    """Hilbert Transform - Sine Wave"""
    try:
        logger.info("Calculating Hilbert Transform - Sine Wave...")
        sine_data, leadsine_data = talib.HT_SINE(data)
        df = pd.DataFrame()
        df['sine'] = sine_data
        df['leadsine'] = leadsine_data
        return df
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def hilbert_transform_trend_vs_cycle_mode(data):
    """Hilbert Transform - Trend vs cycle mode"""
    try:
        logger.info("Calculating Hilbert Transform - Trend vs cycle mode...")
        httc_data = talib.HT_TRENDMODE(data)
        return httc_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def parabolic_sar(high, low, af_step=.02, af_max=.2):
    """Parabolic SAR"""
    try:
        logger.info('Calculating Parabolic SAR...')
        check_inputs_length(high, low)
        ps_data = talib.SAR(high, low, acceleration, maximum)
        return ps_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception

def linear_regression(data, period):
    """Linear Regression"""
    try:
        logger.info(
            'Calculating Linear Regression for period = {}'.format(period))
        check_period_type(period)
        
        lr_data = talib.LINEARREG(data, timeperiod=period)
        return lr_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def linear_regression_angle(data, period):
    """Linear Regression Angle"""
    try:
        logger.info(
            'Calculating Linear Regression Angle for period = {}'.format(
                period))
        check_period_type(period)
        
        lra_data = talib.LINEARREG_ANGLE(data, timeperiod=period)
        return lra_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def linear_regression_intercept(data, period):
    """Linear Regression Intercept"""
    try:
        logger.info(
            'Calculating Linear Regression Intercept for period = {}'.format(
                period))
        check_period_type(period)
        
        lri_data = talib.LINEARREG_INTERCEPT(data, timeperiod=period)
        return lri_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def linear_regression_slope(data, period):
    """Linear Regression Slope"""
    try:
        logger.info(
            'Calculating Linear Regression Slope for period = {}'.format(
                period))
        check_period_type(period)
        
        lrs_data = talib.LINEARREG_SLOPE(data, timeperiod=period)
        return lrs_data
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception

def midpoint_over_period(data, period):
    """Midpoint over period"""
    try:
        logger.info(
            'Calculating Midpoint Over Period for period = {}'.format(period))
        check_period_type(period)
        
        mop = talib.MIDPOINT(data, timeperiod=period)
        return mop
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def midpoint_price_over_period(high, low, period):
    """Midpoint price over period"""
    try:
        logger.info(
            'Calculating Midpoint Price Over Period for period = {}'.format(
                period))
        check_period_type(period)
            
        check_inputs_length(high, low)
        mpop = talib.MIDPRICE(high, low, timeperiod=period)
        return mpop
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception



'''