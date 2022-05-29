package de.yunling.XingzeCraftDriveMod.mixin;

import net.minecraft.client.gui.screen.TitleScreen;

import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

import de.yunling.XingzeCraftDriveMod.XingzeCraftDriveMod;

@Mixin(TitleScreen.class)
public class XingzeCraftDriveModMixin {
	@Inject(at = @At("HEAD"), method = "init()V")
	private void init(CallbackInfo info) {
		XingzeCraftDriveMod.LOGGER.info("XingzeCraftDriveMod is loaded! Beta0.1");
	}
}
